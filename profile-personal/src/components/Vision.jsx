import React from 'react';
import { FiTarget, FiTrendingUp, FiHeart, FiZap } from 'react-icons/fi';
import { motion } from 'framer-motion';
import './Vision.css';

const Vision = () => {
  const visionPoints = [
    {
      icon: <FiTarget />,
      title: 'Brand Recognition',
      description: 'Establish Boka\'s Yarn Market as a globally recognized brand celebrated for creativity, quality, and innovation in handmade fashion.'
    },
    {
      icon: <FiTrendingUp />,
      title: 'Business Growth',
      description: 'Scale the business to reach international markets while maintaining the personal touch and quality that defines our brand.'
    },
    {
      icon: <FiHeart />,
      title: 'Inspire Others',
      description: 'Motivate and inspire young entrepreneurs to pursue their passions with confidence and turn their dreams into reality.'
    },
    {
      icon: <FiZap />,
      title: 'Tech Integration',
      description: 'Merge technology with fashion by leveraging IT skills to create innovative solutions for the handmade crafts industry.'
    }
  ];

  const goals = [
    {
      category: 'Short-term Goals',
      items: [
        'Expand product line with new crochet designs',
        'Increase social media engagement by 50%',
        'Complete Computer Science degree with excellence',
        'Launch e-commerce platform for online sales'
      ]
    },
    {
      category: 'Long-term Goals',
      items: [
        'Open physical retail location for Boka\'s Yarn Market',
        'Develop mobile app for custom design orders',
        'Create educational content teaching crochet skills',
        'Build a team of skilled artisans'
      ]
    }
  ];

  return (
    <section id="vision" className="vision section">
      <div className="container">
        <motion.div
          className="section-header scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="section-title">Vision & Goals</h2>
          <p className="section-subtitle">
            Building the future, one stitch and one line of code at a time
          </p>
        </motion.div>

        {/* Vision Statement */}
        <motion.div
          className="vision-statement scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.2 }}
        >
          <div className="statement-card card">
            <div className="statement-icon">✨</div>
            <h3 className="statement-title gradient-text">My Vision</h3>
            <p className="statement-text">
              I envision a future where <strong>Boka's Yarn Market</strong> stands as a beacon of 
              creativity and quality in the handmade fashion industry. By merging my passion for 
              technology with the timeless art of crochet, I aim to revolutionize how people 
              experience and appreciate handcrafted products.
            </p>
            <p className="statement-text">
              I see a strong connection between my love for IT and crochet—both demand patience, 
              problem-solving, and the ability to build something meaningful from the ground up. 
              This unique perspective drives me to create innovative solutions that bridge the gap 
              between traditional craftsmanship and modern technology.
            </p>
            <p className="statement-text">
              My ultimate goal is to inspire the next generation of young entrepreneurs, showing 
              them that with dedication, creativity, and confidence, any dream is achievable. 
              Whether through code or crochet, I'm committed to making a lasting impact.
            </p>
          </div>
        </motion.div>

        {/* Vision Points */}
        <div className="vision-points grid-2">
          {visionPoints.map((point, index) => (
            <motion.div
              key={index}
              className="vision-point card scroll-reveal"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.1 * index }}
            >
              <div className="point-icon">{point.icon}</div>
              <h4 className="point-title">{point.title}</h4>
              <p className="point-description">{point.description}</p>
            </motion.div>
          ))}
        </div>

        {/* Goals Section */}
        <div className="goals-section">
          {goals.map((goalCategory, categoryIndex) => (
            <motion.div
              key={categoryIndex}
              className="goals-category scroll-reveal"
              initial={{ opacity: 0, x: categoryIndex === 0 ? -30 : 30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.2 }}
            >
              <div className="goals-card card">
                <h3 className="goals-title">{goalCategory.category}</h3>
                <ul className="goals-list">
                  {goalCategory.items.map((item, itemIndex) => (
                    <motion.li
                      key={itemIndex}
                      className="goal-item"
                      initial={{ opacity: 0, x: -20 }}
                      whileInView={{ opacity: 1, x: 0 }}
                      viewport={{ once: true }}
                      transition={{ duration: 0.4, delay: itemIndex * 0.1 }}
                    >
                      <span className="goal-check">✓</span>
                      <span className="goal-text">{item}</span>
                    </motion.li>
                  ))}
                </ul>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Quote Section */}
        <motion.div
          className="quote-section scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          <div className="quote-card">
            <div className="quote-icon">"</div>
            <blockquote className="quote-text">
              Success is not just about what you accomplish, but about what you inspire others 
              to do. Every stitch I create and every line of code I write is a step toward 
              building a legacy of creativity, innovation, and empowerment.
            </blockquote>
            <p className="quote-author">— Bokamoso Sebake</p>
          </div>
        </motion.div>

        {/* Call to Action */}
        <motion.div
          className="vision-cta scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          <div className="cta-content">
            <h3 className="cta-heading">Let's Build the Future Together</h3>
            <p className="cta-description">
              Whether you're looking for unique handmade products, seeking collaboration 
              opportunities, or interested in my technical skills, I'd love to connect with you.
            </p>
            <a href="#contact" className="btn-primary">Get In Touch</a>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default Vision;
