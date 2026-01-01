import React, { useEffect, useRef } from 'react';
import { FiDownload, FiMail, FiArrowDown } from 'react-icons/fi';
import { motion } from 'framer-motion';
import heroImage1 from '../assets/images/hero-image1.jpg.jpeg';
import heroImage2 from '../assets/images/hero-image2.jpg.jpeg';
import heroImage3 from '../assets/images/hero-image3.jpg.jpeg';
import './Hero.css';

const Hero = () => {
  const canvasRef = useRef(null);

  // Particle effect
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const particleCount = 50;

    class Particle {
      constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 3 + 1;
        this.speedX = Math.random() * 1 - 0.5;
        this.speedY = Math.random() * 1 - 0.5;
        this.opacity = Math.random() * 0.5 + 0.2;
      }

      update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.x > canvas.width) this.x = 0;
        if (this.x < 0) this.x = canvas.width;
        if (this.y > canvas.height) this.y = 0;
        if (this.y < 0) this.y = canvas.height;
      }

      draw() {
        ctx.fillStyle = `rgba(139, 92, 246, ${this.opacity})`;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }

    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(particle => {
        particle.update();
        particle.draw();
      });
      requestAnimationFrame(animate);
    }

    animate();

    const handleResize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const handleDownload = (type) => {
    // This will download the placeholder PDFs from the public folder
    const link = document.createElement('a');
    link.href = `/${type}.pdf`;
    link.download = `Bokamoso_Sebake_${type}.pdf`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const scrollToContact = () => {
    const contactSection = document.querySelector('#contact');
    if (contactSection) {
      contactSection.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section id="home" className="hero">
      <canvas ref={canvasRef} className="particle-canvas"></canvas>
      <div className="hero-container">
        <motion.div
          className="hero-content"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <motion.div
            className="hero-badge"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2, duration: 0.5 }}
          >
            <span className="badge-dot"></span>
            Available for Opportunities
          </motion.div>

          <motion.h1
            className="hero-title"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3, duration: 0.8 }}
          >
            Hi, I'm <span className="gradient-text">Bokamoso Sebake</span>
          </motion.h1>

          <motion.h2
            className="hero-subtitle"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4, duration: 0.8 }}
          >
            Founder of Boka's Yarn Market | Computer Science Student
          </motion.h2>

          <motion.p
            className="hero-description"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5, duration: 0.8 }}
          >
            Transforming creativity into reality through crochet artistry and technology.
            Building a brand that celebrates handmade excellence while pursuing innovation
            in Computer Science.
          </motion.p>

          <motion.div
            className="hero-buttons"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6, duration: 0.8 }}
          >
            <button className="btn-primary" onClick={scrollToContact}>
              <FiMail /> Get In Touch
            </button>
            
            <div className="dropdown">
              <button className="btn-secondary">
                <FiDownload /> Download Documents
              </button>
              <div className="dropdown-content">
                <button onClick={() => handleDownload('resume')}>
                  <FiDownload /> Resume
                </button>
                <button onClick={() => handleDownload('cv')}>
                  <FiDownload /> CV
                </button>
                <button onClick={() => handleDownload('cover-letter')}>
                  <FiDownload /> Cover Letter
                </button>
              </div>
            </div>
          </motion.div>

          <motion.div
            className="hero-stats"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.7, duration: 0.8 }}
          >
            <div className="stat-item">
              <h3 className="stat-number gradient-text">5+</h3>
              <p className="stat-label">Years Experience</p>
            </div>
            <div className="stat-divider"></div>
            <div className="stat-item">
              <h3 className="stat-number gradient-text">100+</h3>
              <p className="stat-label">Happy Customers</p>
            </div>
            <div className="stat-divider"></div>
            <div className="stat-item">
              <h3 className="stat-number gradient-text">2019</h3>
              <p className="stat-label">Founded at Age 14</p>
            </div>
          </motion.div>
        </motion.div>

        <motion.div
          className="hero-visual"
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.4, duration: 0.8 }}
        >
          <div className="visual-circle circle-1"></div>
          <div className="visual-circle circle-2"></div>
          <div className="visual-circle circle-3"></div>
          {/* Replaced placeholder with side-by-side images */}
          <div className="hero-images">
            <img src={heroImage1} alt="Bokamoso Sebake - Professional 1" className="hero-image" />
            <img src={heroImage2} alt="Bokamoso Sebake - Professional 2" className="hero-image" />
            <img src={heroImage3} alt="Bokamoso Sebake - Professional 3" className="hero-image" />
          </div>
        </motion.div>
      </div>

      <motion.div
        className="scroll-indicator"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1, duration: 0.8 }}
      >
        <FiArrowDown className="scroll-icon animate-bounce" />
      </motion.div>

      {/* Floating Elements */}
      <div className="floating-elements">
        <div className="float-element element-1">✨</div>
        <div className="float-element element-2">🧶</div>
        <div className="float-element element-3">💻</div>
        <div className="float-element element-4">🎨</div>
      </div>
    </section>
  );
};

export default Hero;
