function toggleSidebar() {
    let sidebar_button = document.getElementById("sidebar-button");
    let sidebar = document.getElementById("sidebar");
    if (sidebar.classList.contains("sidebar-show")) {
        sidebar.classList.remove("sidebar-show");
        sidebar_button.classList.remove("sidebar-button-show");
    } else {
        sidebar.classList.add("sidebar-show");
        sidebar_button.classList.add("sidebar-button-show");
    }
}