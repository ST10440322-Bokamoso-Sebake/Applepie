import React from 'react';
import { FiHeart, FiInstagram, FiMail, FiArrowUp } from 'react-icons/fi';
import { FaFacebook, FaTiktok, FaWhatsapp } from 'react-icons/fa';
import './Footer.css';

const Footer = () => {
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  const quickLinks = [
    { name: 'Home', href: '#home' },
    { name: 'About', href: '#about' },
    { name: 'Achievements', href: '#achievements' },
    { name: 'Skills', href: '#skills' },
    { name: 'Projects', href: '#projects' },
    { name: 'Vision', href: '#vision' },
    { name: 'Contact', href: '#contact' }
  ];

  const socialLinks = [
    { icon: <FiInstagram />, link: 'https://instagram.com/bokamoso', label: 'Instagram' },
    { icon: <FaTiktok />, link: 'https://tiktok.com/@bokamoso', label: 'TikTok' },
    { icon: <FaFacebook />, link: 'https://facebook.com/bokasyarnmarket', label: 'Facebook' },
    { icon: <FaWhatsapp />, link: 'https://wa.me/27793200067', label: 'WhatsApp' }
  ];

  return (
    <footer className="footer">
      <div className="footer-container">
        {/* Main Footer Content */}
        <div className="footer-content">
          {/* Brand Section */}
          <div className="footer-section footer-brand">
            <h3 className="footer-logo gradient-text">Bokamoso Sebake</h3>
            <p className="footer-tagline">
              Founder of Boka's Yarn Market | Computer Science Student
            </p>
            <p className="footer-description">
              Transforming creativity into reality through crochet artistry and technology.
              Building a brand that celebrates handmade excellence.
            </p>
            <div className="footer-social">
              {socialLinks.map((social, index) => (
                <a
                  key={index}
                  href={social.link}
                  className="footer-social-link"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label={social.label}
                >
                  {social.icon}
                </a>
              ))}
            </div>
          </div>

          {/* Quick Links */}
          <div className="footer-section">
            <h4 className="footer-title">Quick Links</h4>
            <ul className="footer-links">
              {quickLinks.map((link, index) => (
                <li key={index}>
                  <a href={link.href} className="footer-link">
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact Info */}
          <div className="footer-section">
            <h4 className="footer-title">Get In Touch</h4>
            <ul className="footer-contact">
              <li>
                <FiMail className="footer-icon" />
                <a href="mailto:rainbow11272005@gmail.com" className="footer-link">
                  rainbow11272005@gmail.com
                </a>
              </li>
              <li>
                <FaWhatsapp className="footer-icon" />
                <a href="tel:+27793200067" className="footer-link">
                  079 320 0067
                </a>
              </li>
            </ul>
            <div className="footer-cta">
              <p className="footer-cta-text">Ready to work together?</p>
              <a href="#contact" className="footer-cta-button">
                Let's Connect
              </a>
            </div>
          </div>
        </div>

        {/* Footer Bottom */}
        <div className="footer-bottom">
          <div className="footer-bottom-content">
            <p className="footer-copyright">
              © {new Date().getFullYear()} Bokamoso Sebake. All rights reserved.
            </p>
            <p className="footer-made-with">
              Made with <FiHeart className="heart-icon" /> and lots of creativity
            </p>
          </div>
        </div>

        {/* Scroll to Top Button */}
        <button
          className="scroll-to-top"
          onClick={scrollToTop}
          aria-label="Scroll to top"
        >
          <FiArrowUp />
        </button>
      </div>
    </footer>
  );
};

export default Footer;
