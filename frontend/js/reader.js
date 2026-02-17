// Reader Module
const reader = {
    currentBook: null,
    currentChapter: null,
    highlights: {},
    selectedVerse: null,

    async init() {
        await this.loadBooks();
        await this.loadHighlights();
        this.setupEventListeners();
    },

    async loadBooks() {
        const books = await api.getBooks();
        const bookSelect = document.getElementById('bookSelect');
        
        books.forEach(book => {
            const option = document.createElement('option');
            option.value = book.id;
            option.textContent = book.name;
            option.dataset.chapterCount = book.chapter_count;
            bookSelect.appendChild(option);
        });
    },

    async loadHighlights() {
        const highlightsData = await api.getHighlights();
        this.highlights = {};
        highlightsData.forEach(h => {
            this.highlights[h.verse] = { id: h.id, color: h.color };
        });
    },

    setupEventListeners() {
        const bookSelect = document.getElementById('bookSelect');
        const chapterSelect = document.getElementById('chapterSelect');
        const verseNumberToggle = document.getElementById('verseNumberToggle');

        bookSelect.addEventListener('change', (e) => {
            const selectedOption = e.target.options[e.target.selectedIndex];
            const chapterCount = parseInt(selectedOption.dataset.chapterCount);
            
            chapterSelect.innerHTML = '<option value="">Select Chapter...</option>';
            
            if (chapterCount) {
                for (let i = 1; i <= chapterCount; i++) {
                    const option = document.createElement('option');
                    option.value = i;
                    option.textContent = `Chapter ${i}`;
                    chapterSelect.appendChild(option);
                }
            }
            
            this.currentBook = e.target.value;
        });

        chapterSelect.addEventListener('change', (e) => {
            this.currentChapter = e.target.value;
            if (this.currentBook && this.currentChapter) {
                this.loadVerses(this.currentBook, this.currentChapter);
            }
        });

        verseNumberToggle.addEventListener('change', (e) => {
            const verseNumbers = document.querySelectorAll('.verse-number');
            verseNumbers.forEach(num => {
                num.style.display = e.target.checked ? 'inline' : 'none';
            });
        });

        // Highlight palette listeners
        const colorButtons = document.querySelectorAll('.color-btn');
        colorButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const color = e.target.dataset.color;
                if (this.selectedVerse) {
                    if (color) {
                        this.addHighlight(this.selectedVerse, color);
                    } else {
                        this.removeHighlight(this.selectedVerse);
                    }
                }
                this.hideHighlightPalette();
            });
        });

        // Close palette on outside click
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.highlight-palette') && !e.target.closest('.verse')) {
                this.hideHighlightPalette();
            }
        });
    },

    async loadVerses(bookId, chapter) {
        const verses = await api.getVerses(bookId, chapter);
        const container = document.getElementById('verseContainer');
        container.innerHTML = '';

        verses.forEach(verse => {
            const verseSpan = document.createElement('span');
            verseSpan.className = 'verse';
            verseSpan.dataset.verseId = verse.id;
            
            const verseNumber = document.createElement('sup');
            verseNumber.className = 'verse-number';
            verseNumber.textContent = verse.verse_number;
            
            verseSpan.appendChild(verseNumber);
            verseSpan.appendChild(document.createTextNode(verse.text + ' '));
            
            // Apply highlight if exists
            if (this.highlights[verse.id]) {
                verseSpan.classList.add(`highlight-${this.highlights[verse.id].color}`);
            }
            
            // Add click listener
            verseSpan.addEventListener('click', (e) => {
                e.stopPropagation();
                this.handleVerseClick(verse.id, e);
            });

            // Add double-click listener for notes
            verseSpan.addEventListener('dblclick', (e) => {
                e.stopPropagation();
                this.showNoteModal(verse.id);
            });
            
            container.appendChild(verseSpan);
        });

        // Save reading progress
        if (verses.length > 0) {
            await api.saveProgress(verses[0].id);
        }
    },

    handleVerseClick(verseId, event) {
        this.selectedVerse = verseId;
        this.showHighlightPalette(event.clientX, event.clientY);
    },

    showHighlightPalette(x, y) {
        const palette = document.getElementById('highlightPalette');
        palette.style.left = `${x}px`;
        palette.style.top = `${y}px`;
        palette.classList.remove('hidden');
    },

    hideHighlightPalette() {
        const palette = document.getElementById('highlightPalette');
        palette.classList.add('hidden');
        this.selectedVerse = null;
    },

    async addHighlight(verseId, color) {
        const result = await api.addHighlight(verseId, color);
        if (result) {
            this.highlights[verseId] = { id: result.id, color: color };
            this.updateVerseHighlight(verseId, color);
        }
    },

    async removeHighlight(verseId) {
        const highlight = this.highlights[verseId];
        if (highlight) {
            const success = await api.deleteHighlight(highlight.id);
            if (success) {
                delete this.highlights[verseId];
                this.updateVerseHighlight(verseId, null);
            }
        }
    },

    updateVerseHighlight(verseId, color) {
        const verseEl = document.querySelector(`[data-verse-id="${verseId}"]`);
        if (verseEl) {
            verseEl.className = 'verse';
            if (color) {
                verseEl.classList.add(`highlight-${color}`);
            }
        }
    },

    showNoteModal(verseId) {
        this.selectedVerse = verseId;
        const modal = document.getElementById('noteModal');
        const noteText = document.getElementById('noteText');
        noteText.value = '';
        modal.classList.remove('hidden');
    },

    hideNoteModal() {
        const modal = document.getElementById('noteModal');
        modal.classList.add('hidden');
        this.selectedVerse = null;
    }
};
