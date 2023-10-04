class TaxonSelect {
    constructor(element, taxon) {
        if (typeof(element) === 'string') {
            element = document.querySelector(element);
        }

        this.selectedTaxon = {
            name: '<i>Euphorbia</i> × <i>martinii</i> \'Ascot Rainbow\'',
            strippedName: 'Euphorbia x martinii \'Ascot Rainbow\'',
            id: 10,
        };

        this.focus = false;

        this.element = element;
        this.taxon = element.querySelector('.ll-taxon-input-taxon');
        this.input = element.querySelector('.ll-taxon-input-input');
        this.value = element.querySelector('.ll-taxon-input-value');
        this.results = element.querySelector('.ll-taxon-input-results');

        this.taxon.addEventListener('click', (e) => this.onTaxonClick(e));
        this.input.addEventListener('focusout', (e) => this.onTaxonFocusOut(e));
        this.input.addEventListener('keydown', (e) => this.onTaxonKeyDown(e));
        this.results.addEventListener('mouseenter', (e) => this.focus = true);
        this.results.addEventListener('mouseleave', (e) => { this.focus = false; this.onTaxonFocusOut(e) });
    }

    async updateSearch(event) {
        let q = encodeURIComponent(this.input.value);
        const response = await fetch(`/taxon/search?q=${q}`);
        const results = await response.json();

        for (var result of results.results) {
            let li = document.createElement('li');
            li.dataset.id = result.id;
            li.dataset.rank = result.rankOrder;
            li.dataset.stripped = result.strippedName;

            li.innerHTML += `<span class="uk-text-meta">${result.rankName}</span><br>`;
            li.innerHTML += `<span class="uk-text-lead">${result.name}</span>`;

            li.addEventListener('click', (e) => {
                this.selectedTaxon.id = li.dataset.id;
                this.selectedTaxon.name = li.querySelector('.uk-text-lead').innerHTML;
                this.selectedTaxon.strippedName = li.dataset.stripped;

                this.focus = false;
                this.onTaxonFocusOut(e);
            });

            this.results.appendChild(li);
        }
    }

    onTaxonClick(event) {
        this.taxon.setAttribute('hidden', '');

        this.results.innerHTML = '';
        this.results.removeAttribute('hidden');

        this.input.value = this.selectedTaxon.strippedName;
        this.input.removeAttribute('hidden');
        this.input.focus();
    }

    onTaxonFocusOut(event) {
        if (document.activeElement === this.input) {
            return
        }

        this.input.setAttribute('hidden', '');

        if (!this.focus) {
            this.results.setAttribute('hidden', '');
        }

        this.taxon.innerHTML = this.selectedTaxon.name;
        this.taxon.removeAttribute('hidden');
    }

    onTaxonKeyDown(event) {
        clearTimeout(this.searchTimeout);
        this.searchTimeout = setTimeout((e) => this.updateSearch(e), 500);
    }
}
