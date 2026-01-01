import React, { useState, useEffect } from 'react';
import { FiMenu, FiX, FiSun, FiMoon } from 'react-icons/fi';
import bannerLogo from '../assets/images/bokas-yarn-market-banner.png.jpeg';
import iconLogo from '../assets/images/boka-yarn-market-icon.png.jpeg';
import './Header.css';

const Header = ({ theme, toggleTheme }) => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navItems = [
    { name: 'Home', href: '#home' },
    { name: 'About', href: '#about' },
    { name: 'Achievements', href: '#achievements' },
    { name: 'Skills', href: '#skills' },
    { name: 'Services', href: '#services' },
    { name: 'Projects', href: '#projects' },
    { name: 'Testimonials', href: '#testimonials' },
    { name: 'Vision', href: '#vision' },
    { name: 'Contact', href: '#contact' }
  ];

  const handleNavClick = (e, href) => {
    e.preventDefault();
    setIsMobileMenuOpen(false); // Close sidebar on nav click
    const element = document.querySelector(href);
    if (element) {
      const offset = 80;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - offset;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  };

  return (
    <>
      <header className={`header ${isScrolled ? 'scrolled' : ''}`}>
        <div className="header-container">
          <div className="logo">
            {/* Banner logo visible on desktop */}
            <img src={bannerLogo} alt="Boka's Yarn Market" className="logo-banner" />
            {/* Icon logo visible on mobile */}
            <img src={iconLogo} alt="Boka's Yarn Market Icon" className="logo-icon" />
          </div>

          {/* Desktop nav - hidden on mobile */}
          <nav className="nav">
            {navItems.map((item, index) => (
              <a
                key={index}
                href={item.href}
                className="nav-link"
                onClick={(e) => handleNavClick(e, item.href)}
              >
                {item.name}
              </a>
            ))}
          </nav>

          <div className="header-actions">
            {/* Theme toggle button */}
            <button
              className="theme-toggle"
              onClick={toggleTheme}
              aria-label="Toggle theme"
            >
              {theme === 'light' ? <FiMoon size={20} /> : <FiSun size={20} />}
            </button>

            {/* Mobile menu toggle button */}
            <button
              className="mobile-menu-toggle"
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              aria-label="Toggle menu"
            >
              {isMobileMenuOpen ? <FiX size={24} /> : <FiMenu size={24} />}
            </button>
          </div>
        </div>
      </header>

      {/* Sidebar Overlay and Menu (only rendered when open) */}
      {isMobileMenuOpen && (
        <>
          <div
            className="sidebar-overlay"
            onClick={() => setIsMobileMenuOpen(false)}
            aria-label="Close menu"
          ></div>
          <div className="sidebar">
            <div className="sidebar-header">
              <button
                className="sidebar-close"
                onClick={() => setIsMobileMenuOpen(false)}
                aria-label="Close menu"
              >
                <FiX size={24} />
              </button>
              {/* Optional secondary theme toggle in sidebar */}
              <button
                className="theme-toggle sidebar-theme-toggle"
                onClick={toggleTheme}
                aria-label="Toggle theme"
              >
                {theme === 'light' ? <FiMoon size={20} /> : <FiSun size={20} />}
              </button>
            </div>

            <nav className="sidebar-nav">
              {navItems.map((item, index) => (
                <a
                  key={index}
                  href={item.href}
                  className="sidebar-nav-link"
                  onClick={(e) => handleNavClick(e, item.href)}
                >
                  {item.name}
                </a>
              ))}
            </nav>
          </div>
        </>
      )}
    </>
  );
};

export default Header;
