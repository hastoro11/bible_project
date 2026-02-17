// API Configuration
const API_BASE_URL = 'http://localhost:8000/api';

// API Helper Functions
const api = {
    // Bible API
    async getBooks() {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/books/`);
            const data = await response.json();
            return data.results || data; // Handle paginated response
        } catch (error) {
            console.error('Error fetching books:', error);
            return [];
        }
    },

    async getChapters(bookId) {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/books/${bookId}/chapters/`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching chapters:', error);
            return null;
        }
    },

    async getVerses(bookId, chapter) {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/verses/?book=${bookId}&chapter=${chapter}`);
            const data = await response.json();
            return data.results || data; // Handle paginated response
        } catch (error) {
            console.error('Error fetching verses:', error);
            return [];
        }
    },

    async searchVerses(query) {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/verses/search/?q=${encodeURIComponent(query)}`);
            return await response.json();
        } catch (error) {
            console.error('Error searching verses:', error);
            return [];
        }
    },

    // Highlights API
    async getHighlights() {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/highlights/`);
            const data = await response.json();
            return data.results || data; // Handle paginated response
        } catch (error) {
            console.error('Error fetching highlights:', error);
            return [];
        }
    },

    async addHighlight(verseId, color) {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/highlights/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ verse: verseId, color: color })
            });
            return await response.json();
        } catch (error) {
            console.error('Error adding highlight:', error);
            return null;
        }
    },

    async deleteHighlight(highlightId) {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/highlights/${highlightId}/`, {
                method: 'DELETE'
            });
            return response.ok;
        } catch (error) {
            console.error('Error deleting highlight:', error);
            return false;
        }
    },

    // Notes API
    async getNotes() {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/notes/`);
            const data = await response.json();
            return data.results || data; // Handle paginated response
        } catch (error) {
            console.error('Error fetching notes:', error);
            return [];
        }
    },

    async addNote(verseId, content) {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/notes/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ verse: verseId, content: content })
            });
            return await response.json();
        } catch (error) {
            console.error('Error adding note:', error);
            return null;
        }
    },

    // Progress API
    async saveProgress(verseId) {
        try {
            const response = await fetch(`${API_BASE_URL}/bible/progress/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ verse: verseId })
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving progress:', error);
            return null;
        }
    },

    // Reading Plans API
    async getReadingPlans() {
        try {
            const response = await fetch(`${API_BASE_URL}/reading/plans/`);
            const data = await response.json();
            return data.results || data; // Handle paginated response
        } catch (error) {
            console.error('Error fetching reading plans:', error);
            return [];
        }
    },

    async getReadingPlan(planId) {
        try {
            const response = await fetch(`${API_BASE_URL}/reading/plans/${planId}/`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching reading plan:', error);
            return null;
        }
    },

    async createReadingPlan(planData) {
        try {
            const response = await fetch(`${API_BASE_URL}/reading/plans/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(planData)
            });
            return await response.json();
        } catch (error) {
            console.error('Error creating reading plan:', error);
            return null;
        }
    },

    async completeDay(planId, dayId) {
        try {
            const response = await fetch(`${API_BASE_URL}/reading/plans/${planId}/complete_day/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ day_id: dayId })
            });
            return await response.json();
        } catch (error) {
            console.error('Error completing day:', error);
            return null;
        }
    }
};
