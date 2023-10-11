class Taxon {
    static async get(id) {
        const response = await fetch(`/api/taxon/${id}`);

        if (response.status != 200) {
            return null;
        }

        const result = await response.json();

        return result;
    }
}

class TaxonSelect {
    constructor(element, taxon) {
        this.searchTimeout = null;

        /* Set up class events */
        this.eventProxy = document.createDocumentFragment();
        this.eventProxy.host = this;

        ['addEventListener', 'dispatchEvent', 'removeEventListener'].forEach(
            this.delegate,
            this
        );

        /* Create DOM elements */
        if (typeof(element) === 'string') {
            element = document.querySelector(element);
        }

        this.input = element;

        this.displayNameContainer = document.createElement('div');
        this.displayNameContainer.classList.add('uk-search');
        this.displayNameContainer.classList.add('uk-width-1-1');
        this.displayNameContainer.classList.add('uk-search-default');
 
        this.displayName = document.createElement('div');
        this.displayName.classList.add('uk-input');
        this.displayName.classList.add('ll-taxonselect-displayname');
        this.displayName.addEventListener('click', (e) => this.onDisplayNameClick());
        this.displayName.innerHTML = '(none)';
        this.displayNameContainer.appendChild(this.displayName);

        this.clearButton = document.createElement('a');
        this.clearButton.classList.add('uk-form-icon');
        this.clearButton.classList.add('uk-form-icon-flip');
        this.clearButton.setAttribute('uk-icon', 'icon: close');
        this.clearButton.addEventListener('click', (e) => this.clear());
        this.displayNameContainer.appendChild(this.clearButton);

        this.input.after(this.displayNameContainer);

        this.inputSearchContainer = document.createElement('div');
        this.inputSearchContainer.classList.add('uk-search');
        this.inputSearchContainer.classList.add('uk-width-1-1');
        this.inputSearchContainer.classList.add('uk-search-default');
        this.inputSearchContainer.setAttribute('hidden', '');
        
        this.inputSearchIcon = document.createElement('a');
        this.inputSearchIcon.classList.add('uk-form-icon');
        this.inputSearchIcon.classList.add('uk-form-icon-flip');
        this.inputSearchIcon.setAttribute('uk-icon', 'icon: search');
        this.inputSearchIcon.addEventListener('click', (e) => this.hideSearch());
        this.inputSearchContainer.appendChild(this.inputSearchIcon);

        this.inputSearch = document.createElement('input');
        this.inputSearch.classList.add('uk-search-input');
        this.inputSearch.setAttribute('type', 'search');
        this.inputSearch.addEventListener('keydown', (e) => {
            clearTimeout(this.searchTimeout);
            this.searchTimeout = setTimeout((e) => this.updateSearch(), 500);
        });
        this.inputSearch.addEventListener('focusout', (e) => this.hideSearch());
        this.inputSearchContainer.appendChild(this.inputSearch);

        this.displayNameContainer.after(this.inputSearchContainer);

        this.searchResults = document.createElement('ul');
        this.searchResults.classList.add('ll-taxonselect-results');
        this.inputSearchContainer.after(this.searchResults);

        /* Update input values */
        if (this.input.value) {
            this.value = this.input.value;
        }
    }

    delegate(method) {
        this.eventProxy.host[method] = this.eventProxy[method].bind(this.eventProxy);
    }

    onDisplayNameClick() {
        this.displayNameContainer.setAttribute('hidden', '');

        this.inputSearchContainer.removeAttribute('hidden');

        if (this.taxon) {
            this.inputSearch.value = this.taxon.displayName;
            this.updateSearch();
        } else {
            this.inputSearch.value = '';
        }

        this.inputSearch.focus();
    }

    hideSearch() {
        this.displayNameContainer.removeAttribute('hidden');
        this.inputSearchContainer.setAttribute('hidden', '');
        this.searchResults.innerHTML = '';
    }

    clear() {
        this.input.value = '';
        this.taxon = null;
        this.displayName.innerHTML = '(none)';
        
        const event = new CustomEvent('change', {'detail': null});
        this.dispatchEvent(event);
    }

    set value(id) {
        this.input.value = id;

        Taxon.get(id).then((data) => {
            this.taxon = data;

            const event = new CustomEvent('change', {'detail': data});
            this.dispatchEvent(event);

            /* Update fields */
            this.displayName.innerHTML = this.taxon.displayNameHtml;
        });
    }

    async updateSearch(event) {
        this.searchResults.innerHTML = '';

        if (!this.inputSearch.value) {
            return
        }

        let q = encodeURIComponent(this.inputSearch.value);
        const response = await fetch(`/api/taxon/search?q=${q}`);
        const results = await response.json();

        for (var result of results.results) {
            let li = document.createElement('li');
            li.innerHTML = `<strong>${result.displayNameHtml}</strong> (${result.rankName})`;
            li.dataset.id = result.id
            li.addEventListener('pointerdown', (e) => {
                this.value = li.dataset.id;
                this.hideSearch();
            });

            this.searchResults.appendChild(li);
        }
    }
}
