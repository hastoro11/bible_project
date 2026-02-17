// Search Module
const search = {
    async init() {
        this.setupEventListeners();
    },

    setupEventListeners() {
        const searchButton = document.getElementById('searchButton');
        const searchInput = document.getElementById('searchInput');

        searchButton.addEventListener('click', () => {
            this.performSearch();
        });

        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.performSearch();
            }
        });
    },

    async performSearch() {
        const searchInput = document.getElementById('searchInput');
        const query = searchInput.value.trim();

        if (!query) {
            return;
        }

        const results = await api.searchVerses(query);
        this.displayResults(results);
    },

    displayResults(results) {
        const container = document.getElementById('searchResults');
        container.innerHTML = '';

        if (results.length === 0) {
            container.innerHTML = '<p style="text-align: center; color: #999;">No results found</p>';
            return;
        }

        results.forEach(verse => {
            const resultDiv = document.createElement('div');
            resultDiv.className = 'search-result';

            const refDiv = document.createElement('div');
            refDiv.className = 'search-result-ref';
            refDiv.textContent = `${verse.book_name} ${verse.chapter}:${verse.verse_number}`;

            const textDiv = document.createElement('div');
            textDiv.className = 'search-result-text';
            textDiv.textContent = verse.text;

            resultDiv.appendChild(refDiv);
            resultDiv.appendChild(textDiv);

            // Add click to navigate to verse
            resultDiv.addEventListener('click', () => {
                this.navigateToVerse(verse);
            });

            container.appendChild(resultDiv);
        });
    },

    navigateToVerse(verse) {
        // Switch to reader tab
        document.getElementById('readerBtn').click();

        // Set book and chapter
        const bookSelect = document.getElementById('bookSelect');
        const chapterSelect = document.getElementById('chapterSelect');

        bookSelect.value = verse.book;
        bookSelect.dispatchEvent(new Event('change'));

        // Wait a bit for chapter select to populate
        setTimeout(() => {
            chapterSelect.value = verse.chapter;
            chapterSelect.dispatchEvent(new Event('change'));

            // Scroll to verse after loading
            setTimeout(() => {
                const verseEl = document.querySelector(`[data-verse-id="${verse.id}"]`);
                if (verseEl) {
                    verseEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    verseEl.style.backgroundColor = '#ffeb3b';
                    setTimeout(() => {
                        verseEl.style.backgroundColor = '';
                    }, 2000);
                }
            }, 500);
        }, 100);
    }
};
