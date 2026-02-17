// Reading Plans Module
const plans = {
    currentPlans: [],

    async init() {
        await this.loadPlans();
        this.setupEventListeners();
    },

    setupEventListeners() {
        const createPlanBtn = document.getElementById('createPlanBtn');
        
        createPlanBtn.addEventListener('click', () => {
            this.showCreatePlanForm();
        });

        // Modal close buttons
        const closeButtons = document.querySelectorAll('.modal .close');
        closeButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.target.closest('.modal').classList.add('hidden');
            });
        });

        // Close modal on outside click
        document.querySelectorAll('.modal').forEach(modal => {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    modal.classList.add('hidden');
                }
            });
        });
    },

    async loadPlans() {
        this.currentPlans = await api.getReadingPlans();
        this.displayPlans();
    },

    displayPlans() {
        const container = document.getElementById('plansContainer');
        container.innerHTML = '';

        if (this.currentPlans.length === 0) {
            container.innerHTML = '<p style="text-align: center; color: #999;">No reading plans yet. Create one to get started!</p>';
            return;
        }

        this.currentPlans.forEach(plan => {
            const card = this.createPlanCard(plan);
            container.appendChild(card);
        });
    },

    createPlanCard(plan) {
        const card = document.createElement('div');
        card.className = 'plan-card';

        const title = document.createElement('h3');
        title.textContent = plan.name;

        const description = document.createElement('p');
        description.textContent = plan.description;

        const dates = document.createElement('p');
        dates.innerHTML = `<strong>Duration:</strong> ${plan.start_date} to ${plan.end_date}`;

        const progress = document.createElement('div');
        progress.className = 'plan-progress';
        
        const progressBar = document.createElement('div');
        progressBar.className = 'plan-progress-bar';
        const percentage = plan.days_count > 0 ? (plan.completed_days / plan.days_count) * 100 : 0;
        progressBar.style.width = `${percentage}%`;
        
        progress.appendChild(progressBar);

        const progressText = document.createElement('p');
        progressText.innerHTML = `<strong>Progress:</strong> ${plan.completed_days} / ${plan.days_count} days`;

        card.appendChild(title);
        card.appendChild(description);
        card.appendChild(dates);
        card.appendChild(progressText);
        card.appendChild(progress);

        card.addEventListener('click', () => {
            this.showPlanDetails(plan.id);
        });

        return card;
    },

    async showPlanDetails(planId) {
        const plan = await api.getReadingPlan(planId);
        if (!plan) return;

        const modal = document.getElementById('planModal');
        const title = document.getElementById('planTitle');
        const content = document.getElementById('planContent');

        title.textContent = plan.name;
        content.innerHTML = '';

        // Plan info
        const info = document.createElement('div');
        info.innerHTML = `
            <p>${plan.description}</p>
            <p><strong>Start Date:</strong> ${plan.start_date}</p>
            <p><strong>End Date:</strong> ${plan.end_date}</p>
            <hr style="margin: 20px 0;">
        `;
        content.appendChild(info);

        // Days
        if (plan.days && plan.days.length > 0) {
            const daysTitle = document.createElement('h3');
            daysTitle.textContent = 'Reading Schedule';
            content.appendChild(daysTitle);

            plan.days.forEach(day => {
                const dayDiv = this.createDayElement(day, plan.id);
                content.appendChild(dayDiv);
            });
        }

        modal.classList.remove('hidden');
    },

    createDayElement(day, planId) {
        const dayDiv = document.createElement('div');
        dayDiv.style.cssText = 'margin: 10px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px;';

        const dayHeader = document.createElement('div');
        dayHeader.style.cssText = 'display: flex; justify-content: space-between; align-items: center;';

        const dayInfo = document.createElement('div');
        dayInfo.innerHTML = `
            <strong>Day ${day.day_number}</strong> - ${day.date}
            ${day.title ? `<br><em>${day.title}</em>` : ''}
        `;

        const completeBtn = document.createElement('button');
        completeBtn.textContent = day.is_completed ? 'Completed ✓' : 'Mark Complete';
        completeBtn.className = 'btn-primary';
        completeBtn.style.padding = '5px 10px';
        completeBtn.style.fontSize = '12px';
        
        if (day.is_completed) {
            completeBtn.disabled = true;
            completeBtn.style.backgroundColor = '#27ae60';
        } else {
            completeBtn.addEventListener('click', async () => {
                await this.completeDay(planId, day.id);
            });
        }

        dayHeader.appendChild(dayInfo);
        dayHeader.appendChild(completeBtn);
        dayDiv.appendChild(dayHeader);

        // Verses
        if (day.verses && day.verses.length > 0) {
            const versesList = document.createElement('div');
            versesList.style.marginTop = '10px';
            versesList.innerHTML = '<strong>Readings:</strong><br>';
            
            day.verses.forEach(v => {
                const verseDetail = v.verse_detail;
                const verseSpan = document.createElement('span');
                verseSpan.textContent = `${verseDetail.book_name} ${verseDetail.chapter}:${verseDetail.verse_number} `;
                versesList.appendChild(verseSpan);
            });
            
            dayDiv.appendChild(versesList);
        }

        return dayDiv;
    },

    async completeDay(planId, dayId) {
        const result = await api.completeDay(planId, dayId);
        if (result) {
            // Reload plan details
            await this.showPlanDetails(planId);
            // Reload plans list
            await this.loadPlans();
        }
    },

    showCreatePlanForm() {
        alert('Plan creation form would be implemented here. For demo purposes, reading plans need to be created via the admin panel at /admin/');
    }
};
