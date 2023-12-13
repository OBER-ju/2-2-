document.addEventListener('DOMContentLoaded', function () {
    const textContainers = document.querySelectorAll('.text-container');
    let activeIndex = 0;
    
        window.addEventListener('scroll', function () {
        const scrollTop = window.scrollY;
    
        textContainers.forEach((container, index) => {
            const containerTop = container.offsetTop;
    
            if (scrollTop >= containerTop) {
            activeIndex = index;
            }
        });
    
        textContainers.forEach((container, index) => {
            container.classList.remove('active');
            if (index === activeIndex) {
            container.classList.add('active');
            }
        });
        });
    });
    
    