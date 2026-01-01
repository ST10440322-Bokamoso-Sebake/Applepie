import React from 'react';
import { FiUser, FiBriefcase, FiHeart, FiTarget } from 'react-icons/fi';
import { motion } from 'framer-motion';
import './About.css';

const About = () => {
  const aboutCards = [
    {
      icon: <FiUser />,
      title: 'Who I Am',
      description: 'A passionate entrepreneur and Computer Science student at Varsity College Midrand, combining creativity with technology.'
    },
    {
      icon: <FiBriefcase />,
      title: 'What I Do',
      description: 'Founder of Boka\'s Yarn Market, specializing in handmade crochet clothing, accessories, and décor with modern fashion aesthetics.'
    },
    {
      icon: <FiHeart />,
      title: 'My Passion',
      description: 'Transforming a childhood hobby into a thriving business, celebrating the art of crochet and the value of handmade products.'
    },
    {
      icon: <FiTarget />,
      title: 'My Mission',
      description: 'Building a recognized brand that merges technology with fashion, inspiring young entrepreneurs to pursue their dreams.'
    }
  ];

  return (
    <section id="about" className="about section">
      <div className="container">
        <motion.div
          className="section-header scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="section-title">About Me</h2>
          <p className="section-subtitle">
            Entrepreneur | Computer Science Student | Creative Innovator
          </p>
        </motion.div>

        <div className="about-content">
          <motion.div
            className="about-main scroll-reveal"
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <div className="about-text-card card">
              <h3 className="about-heading gradient-text">My Story</h3>
              <p className="about-paragraph">
                I'm <strong>Bokamoso Sebake</strong>, the founder of <strong>Boka's Yarn Market</strong>, 
                a crochet and fashion arts & crafts brand that I started in 2019 at just 14 years old. 
                What began as a simple hobby has blossomed into a business that celebrates creativity, 
                uniqueness, and the timeless art of handmade craftsmanship.
              </p>
              <p className="about-paragraph">
                Each piece I create is designed with meticulous attention to detail, blending modern 
                fashion trends with traditional crochet techniques. From custom clothing to unique 
                accessories and beautiful décor, every item tells a story of passion and dedication.
              </p>
              <p className="about-paragraph">
                Currently pursuing Computer Science at Varsity College Midrand, I see a powerful 
                connection between my love for technology and crochet. Both require patience, 
                problem-solving skills, and the ability to build something meaningful from the ground up. 
                This unique perspective allows me to approach both my studies and business with 
                innovation and creativity.
              </p>
              <p className="about-paragraph">
                Through my journey, I've built a growing customer base across Instagram, TikTok, and 
                Facebook, while gaining invaluable skills in branding, marketing, and customer service. 
                Balancing entrepreneurship with my studies has taught me discipline, time management, 
                and the importance of pursuing your passions with unwavering confidence.
              </p>
            </div>
          </motion.div>

          <div className="about-cards grid-2">
            {aboutCards.map((card, index) => (
              <motion.div
                key={index}
                className="about-card card scroll-reveal"
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: 0.1 * index }}
              >
                <div className="card-icon">{card.icon}</div>
                <h4 className="card-title">{card.title}</h4>
                <p className="card-description">{card.description}</p>
              </motion.div>
            ))}
          </div>
        </div>

        <motion.div
          className="about-highlight scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          <div className="highlight-card card">
            <div className="highlight-content">
              <h3 className="highlight-title">Boka's Yarn Market</h3>
              <p className="highlight-text">
                A brand built on creativity, quality, and the celebration of handmade excellence. 
                Every stitch represents dedication, every design tells a story, and every customer 
                becomes part of our growing community of art enthusiasts.
              </p>
              <div className="highlight-features">
                <div className="feature-item">
                  <span className="feature-icon">✨</span>
                  <span>Handcrafted with Love</span>
                </div>
                <div className="feature-item">
                  <span className="feature-icon">🎨</span>
                  <span>Unique Designs</span>
                </div>
                <div className="feature-item">
                  <span className="feature-icon">💎</span>
                  <span>Premium Quality</span>
                </div>
                <div className="feature-item">
                  <span className="feature-icon">🌟</span>
                  <span>Customer Focused</span>
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default About;
