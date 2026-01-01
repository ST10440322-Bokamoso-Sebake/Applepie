import React from 'react';
import { FiAward, FiTrendingUp, FiUsers, FiStar, FiBook, FiShoppingBag } from 'react-icons/fi';
import { motion } from 'framer-motion';
import './Achievements.css';

const Achievements = () => {
  const achievements = [
    {
      icon: <FiAward />,
      title: 'Young Entrepreneur',
      description: 'Founded Boka\'s Yarn Market  in 2019',
      year: '2019',
      color: '#8B5CF6'
    },
    {
      icon: <FiTrendingUp />,
      title: 'Growing Business',
      description: 'Building a thriving customer base across multiple social media platforms',
      year: '2019-2024',
      color: '#A78BFA'
    },
    {
      icon: <FiUsers />,
      title: 'Customer Success',
      description: 'Delivered 100+ custom crochet fashion and décor pieces to satisfied customers',
      year: 'Ongoing',
      color: '#C084FC'
    },
    {
      icon: <FiStar />,
      title: 'Brand Recognition',
      description: 'Established strong presence on Instagram, TikTok, and Facebook',
      year: '2020-2024',
      color: '#DDD6FE'
    },
    {
      icon: <FiBook />,
      title: 'Academic Excellence',
      description: 'Successfully balancing Computer Science studies with entrepreneurship',
      year: 'Current',
      color: '#8B5CF6'
    },
    {
      icon: <FiShoppingBag />,
      title: 'Business Skills',
      description: 'Gained practical expertise in branding, marketing, and customer service',
      year: '2019-2024',
      color: '#A78BFA'
    }
  ];

  const milestones = [
    {
      number: '5+',
      label: 'Years in Business',
      description: 'Since 2019'
    },
    {
      number: '100+',
      label: 'Happy Customers',
      description: 'And growing'
    },
    {
      number: '1000+',
      label: 'Social Media Followers',
      description: 'Across platforms'
    },
    {
      number: '∞',
      label: 'Creative Designs',
      description: 'Unique pieces'
    }
  ];

  return (
    <section id="achievements" className="achievements section">
      <div className="container">
        <motion.div
          className="section-header scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="section-title">Achievements & Milestones</h2>
          <p className="section-subtitle">
            A journey of growth, learning, and success
          </p>
        </motion.div>

        {/* Milestones Stats */}
        <div className="milestones-grid">
          {milestones.map((milestone, index) => (
            <motion.div
              key={index}
              className="milestone-card card scroll-reveal"
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <h3 className="milestone-number gradient-text">{milestone.number}</h3>
              <p className="milestone-label">{milestone.label}</p>
              <p className="milestone-description">{milestone.description}</p>
            </motion.div>
          ))}
        </div>

        {/* Achievement Cards */}
        <div className="achievements-grid">
          {achievements.map((achievement, index) => (
            <motion.div
              key={index}
              className="achievement-card card scroll-reveal"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
            >
              <div className="achievement-header">
                <div 
                  className="achievement-icon"
                  style={{ background: `linear-gradient(135deg, ${achievement.color}, ${achievement.color}dd)` }}
                >
                  {achievement.icon}
                </div>
                <span className="achievement-year">{achievement.year}</span>
              </div>
              <h3 className="achievement-title">{achievement.title}</h3>
              <p className="achievement-description">{achievement.description}</p>
            </motion.div>
          ))}
        </div>

        {/* Timeline */}
        <motion.div
          className="timeline-section scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          <h3 className="timeline-title">My Journey</h3>
          <div className="timeline">
            <div className="timeline-item">
              <div className="timeline-dot"></div>
              <div className="timeline-content">
                <h4 className="timeline-year">2019</h4>
                <p className="timeline-text">Founded Boka's Yarn Market at age 14, turning a hobby into a business</p>
              </div>
            </div>
            <div className="timeline-item">
              <div className="timeline-dot"></div>
              <div className="timeline-content">
                <h4 className="timeline-year">2020-2022</h4>
                <p className="timeline-text">Expanded social media presence and built a loyal customer base</p>
              </div>
            </div>
            <div className="timeline-item">
              <div className="timeline-dot"></div>
              <div className="timeline-content">
                <h4 className="timeline-year">2023</h4>
                <p className="timeline-text">Enrolled in Computer Science at Varsity College Midrand</p>
              </div>
            </div>
            <div className="timeline-item">
              <div className="timeline-dot"></div>
              <div className="timeline-content">
                <h4 className="timeline-year">2024</h4>
                <p className="timeline-text">Successfully balancing studies with growing business operations</p>
              </div>
            </div>
            <div className="timeline-item">
              <div className="timeline-dot active"></div>
              <div className="timeline-content">
                <h4 className="timeline-year">Present</h4>
                <p className="timeline-text">Continuing to innovate and inspire young entrepreneurs</p>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default Achievements;
