import React from 'react';
import { FiCode, FiBriefcase, FiTrendingUp, FiPenTool } from 'react-icons/fi';
import { motion } from 'framer-motion';
import './Skills.css';

const Skills = () => {
  const skillCategories = [
    {
      icon: <FiCode />,
      title: 'Technical Skills',
      color: '#8B5CF6',
      skills: [
        { name: 'Computer Science', level: 85 },
        { name: 'Problem Solving', level: 90 },
        { name: 'Software Development', level: 80 },
        { name: 'Digital Marketing', level: 85 },
        { name: 'Social Media Management', level: 95 }
      ]
    },
    {
      icon: <FiBriefcase />,
      title: 'Business Skills',
      color: '#A78BFA',
      skills: [
        { name: 'Entrepreneurship', level: 95 },
        { name: 'Brand Management', level: 90 },
        { name: 'Customer Service', level: 95 },
        { name: 'Marketing Strategy', level: 85 },
        { name: 'Financial Management', level: 80 }
      ]
    },
    {
      icon: <FiPenTool />,
      title: 'Creative Skills',
      color: '#C084FC',
      skills: [
        { name: 'Crochet Design', level: 98 },
        { name: 'Fashion Design', level: 90 },
        { name: 'Product Photography', level: 85 },
        { name: 'Creative Direction', level: 90 },
        { name: 'Pattern Development', level: 95 }
      ]
    },
    {
      icon: <FiTrendingUp />,
      title: 'Soft Skills',
      color: '#DDD6FE',
      skills: [
        { name: 'Time Management', level: 90 },
        { name: 'Communication', level: 95 },
        { name: 'Adaptability', level: 92 },
        { name: 'Leadership', level: 88 },
        { name: 'Self-Motivation', level: 98 }
      ]
    }
  ];

  const tools = [
    { name: 'Instagram', category: 'Social Media' },
    { name: 'TikTok', category: 'Social Media' },
    { name: 'Facebook', category: 'Social Media' },
    { name: 'Canva', category: 'Design' },
    { name: 'Microsoft Office', category: 'Productivity' },
    { name: 'WhatsApp Business', category: 'Communication' }
  ];

  return (
    <section id="skills" className="skills section">
      <div className="container">
        <motion.div
          className="section-header scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="section-title">Skills & Expertise</h2>
          <p className="section-subtitle">
            A diverse skill set combining creativity, technology, and business acumen
          </p>
        </motion.div>

        <div className="skills-grid">
          {skillCategories.map((category, categoryIndex) => (
            <motion.div
              key={categoryIndex}
              className="skill-category card scroll-reveal"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: categoryIndex * 0.1 }}
            >
              <div className="category-header">
                <div 
                  className="category-icon"
                  style={{ background: `linear-gradient(135deg, ${category.color}, ${category.color}dd)` }}
                >
                  {category.icon}
                </div>
                <h3 className="category-title">{category.title}</h3>
              </div>

              <div className="skills-list">
                {category.skills.map((skill, skillIndex) => (
                  <div key={skillIndex} className="skill-item">
                    <div className="skill-info">
                      <span className="skill-name">{skill.name}</span>
                      <span className="skill-percentage">{skill.level}%</span>
                    </div>
                    <div className="skill-bar">
                      <motion.div
                        className="skill-progress"
                        style={{ background: category.color }}
                        initial={{ width: 0 }}
                        whileInView={{ width: `${skill.level}%` }}
                        viewport={{ once: true }}
                        transition={{ duration: 1, delay: skillIndex * 0.1 }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </motion.div>
          ))}
        </div>

        {/* Tools & Technologies */}
        <motion.div
          className="tools-section scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          <h3 className="tools-title">Tools & Platforms</h3>
          <div className="tools-grid">
            {tools.map((tool, index) => (
              <motion.div
                key={index}
                className="tool-card"
                initial={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: index * 0.05 }}
              >
                <span className="tool-name">{tool.name}</span>
                <span className="tool-category">{tool.category}</span>
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* Key Strengths */}
        <motion.div
          className="strengths-section scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          <div className="strengths-card card">
            <h3 className="strengths-title gradient-text">What Sets Me Apart</h3>
            <div className="strengths-grid">
              <div className="strength-item">
                <div className="strength-icon">🎯</div>
                <h4>Dual Expertise</h4>
                <p>Unique combination of technical knowledge and creative craftsmanship</p>
              </div>
              <div className="strength-item">
                <div className="strength-icon">⚡</div>
                <h4>Young Innovator</h4>
                <p>Fresh perspective with proven entrepreneurial success since age 14</p>
              </div>
              <div className="strength-item">
                <div className="strength-icon">🌟</div>
                <h4>Passionate Creator</h4>
                <p>Deep commitment to quality and attention to detail in every project</p>
              </div>
              <div className="strength-item">
                <div className="strength-icon">🚀</div>
                <h4>Growth Mindset</h4>
                <p>Continuously learning and adapting to new challenges and opportunities</p>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default Skills;
