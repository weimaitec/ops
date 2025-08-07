const { createApp } = Vue;

createApp({
    data() {
        return {
            projects: [],
            selectedProject: null,
            builds: [],
            currentBuild: null,
            currentLog: '',
        };
    },
    methods: {
        async fetchProjects() {
            // Mock data for now
            this.projects = [
                { id: 1, name: 'project-alpha', jenkins_job: 'job-alpha' },
                { id: 2, name: 'project-beta', jenkins_job: 'job-beta' },
                { id: 3, name: 'project-gamma', jenkins_job: 'job-gamma' },
            ];
        },
        selectProject(project) {
            this.selectedProject = project;
            this.fetchBuildHistory(project.id);
            this.currentLog = '';
            this.currentBuild = null;
        },
        async fetchBuildHistory(projectId) {
            // Mock data for now
            this.builds = [
                { id: 101, number: 5, status: 'SUCCESS', timestamp: Date.now() - 100000, user: 'jules' },
                { id: 102, number: 4, status: 'FAILED', timestamp: Date.now() - 200000, user: 'user1' },
                { id: 103, number: 3, status: 'SUCCESS', timestamp: Date.now() - 300000, user: 'user2' },
            ];
        },
        async triggerBuild(project) {
            alert(`Triggering build for ${project.name}...`);
            // In a real app, this would be an API call:
            // await axios.post(`/api/jenkins/jobs/${project.jenkins_job}/build`);
            // And we would update the build history.
        },
        showBuildLog(build) {
            this.currentBuild = build;
            // Mock log data
            this.currentLog = `Starting build #${build.number}...\nFetching from Git...\nRunning tests...\n${build.status === 'SUCCESS' ? 'Build successful!' : 'Build failed!'}\nDone.`;
        }
    },
    mounted() {
        this.fetchProjects();
    }
}).mount('#app');
