// Main Application
document.addEventListener('DOMContentLoaded', async () => {
    // Initialize modules
    await reader.init();
    await search.init();
    await plans.init();

    // Setup navigation
    setupNavigation();

    // Setup note modal
    setupNoteModal();

    console.log('Bible App initialized successfully!');
});

function setupNavigation() {
    const navButtons = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.section');

    navButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons and sections
            navButtons.forEach(b => b.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));

            // Add active class to clicked button
            btn.classList.add('active');

            // Show corresponding section
            const sectionId = btn.id.replace('Btn', 'Section');
            const section = document.getElementById(sectionId);
            if (section) {
                section.classList.add('active');
            }
        });
    });
}

function setupNoteModal() {
    const modal = document.getElementById('noteModal');
    const closeBtn = modal.querySelector('.close');
    const saveBtn = document.getElementById('saveNoteBtn');

    closeBtn.addEventListener('click', () => {
        reader.hideNoteModal();
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            reader.hideNoteModal();
        }
    });

    saveBtn.addEventListener('click', async () => {
        const noteText = document.getElementById('noteText').value.trim();
        if (noteText && reader.selectedVerse) {
            const result = await api.addNote(reader.selectedVerse, noteText);
            if (result) {
                alert('Note saved successfully!');
                reader.hideNoteModal();
            } else {
                alert('Failed to save note. Please try again.');
            }
        }
    });
}
