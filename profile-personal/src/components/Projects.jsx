import React, { useState } from 'react';
import { FiX, FiExternalLink } from 'react-icons/fi';
import { motion, AnimatePresence } from 'framer-motion';
import './Projects.css';

const Projects = () => {
  const [selectedProject, setSelectedProject] = useState(null);
  const [filter, setFilter] = useState('all');

  const projects = [
    {
      id: 1,
      title: 'Custom Crochet Clothing',
      category: 'crochet',
      description: 'Handmade crochet clothing pieces including tops, cardigans, and dresses designed with modern fashion trends.',
      fullDescription: 'Each clothing piece is carefully crafted with premium yarn, featuring unique patterns and designs. From casual wear to statement pieces, every item is customizable to match your style preferences and measurements.',
      image: 'https://via.placeholder.com/400x300/8B5CF6/FFFFFF?text=Crochet+Clothing',
      tags: ['Fashion', 'Handmade', 'Custom'],
      link: '#'
    },
    {
      id: 2,
      title: 'Crochet Accessories',
      category: 'crochet',
      description: 'Beautiful handcrafted accessories including bags, hats, scarves, and jewelry pieces.',
      fullDescription: 'Elevate your style with unique crochet accessories. From trendy bucket hats to elegant bags and statement jewelry, each piece adds a touch of handmade charm to any outfit.',
      image: 'https://via.placeholder.com/400x300/A78BFA/FFFFFF?text=Accessories',
      tags: ['Accessories', 'Fashion', 'Unique'],
      link: '#'
    },
    {
      id: 3,
      title: 'Home Décor Collection',
      category: 'crochet',
      description: 'Cozy and stylish home décor items including blankets, cushions, and wall hangings.',
      fullDescription: 'Transform your living space with handmade crochet décor. Our collection includes plush blankets, decorative cushions, and artistic wall hangings that bring warmth and personality to any room.',
      image: 'https://via.placeholder.com/400x300/C084FC/FFFFFF?text=Home+Decor',
      tags: ['Home', 'Décor', 'Cozy'],
      link: '#'
    },
    {
      id: 4,
      title: 'Social Media Growth',
      category: 'business',
      description: 'Successfully built and managed social media presence across Instagram, TikTok, and Facebook.',
      fullDescription: 'Developed and executed social media strategies that resulted in significant follower growth and engagement. Created compelling content showcasing products and behind-the-scenes processes.',
      image: 'https://via.placeholder.com/400x300/DDD6FE/8B5CF6?text=Social+Media',
      tags: ['Marketing', 'Growth', 'Digital'],
      link: '#'
    },
    {
      id: 5,
      title: 'Brand Development',
      category: 'business',
      description: 'Created and established Boka\'s Yarn Market brand identity from concept to execution.',
      fullDescription: 'Developed comprehensive brand identity including logo design, color schemes, brand voice, and visual aesthetics. Established brand guidelines that maintain consistency across all platforms.',
      image: 'https://via.placeholder.com/400x300/8B5CF6/FFFFFF?text=Branding',
      tags: ['Branding', 'Design', 'Strategy'],
      link: '#'
    },
    {
      id: 6,
      title: 'Computer Science Projects',
      category: 'tech',
      description: 'Various programming and software development projects completed during studies.',
      fullDescription: 'Portfolio of technical projects demonstrating proficiency in programming, problem-solving, and software development. Projects range from web applications to algorithms and data structures.',
      image: 'https://via.placeholder.com/400x300/A78BFA/FFFFFF?text=Tech+Projects',
      tags: ['Programming', 'Development', 'Innovation'],
      link: '#'
    }
  ];

  const categories = [
    { id: 'all', name: 'All Projects' },
    { id: 'crochet', name: 'Crochet Work' },
    { id: 'business', name: 'Business' },
    { id: 'tech', name: 'Technology' }
  ];

  const filteredProjects = filter === 'all' 
    ? projects 
    : projects.filter(project => project.category === filter);

  return (
    <section id="projects" className="projects section">
      <div className="container">
        <motion.div
          className="section-header scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="section-title">Projects & Portfolio</h2>
          <p className="section-subtitle">
            A showcase of my creative work and business achievements
          </p>
        </motion.div>

        {/* Filter Buttons */}
        <motion.div
          className="filter-buttons scroll-reveal"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.2 }}
        >
          {categories.map((category) => (
            <button
              key={category.id}
              className={`filter-btn ${filter === category.id ? 'active' : ''}`}
              onClick={() => setFilter(category.id)}
            >
              {category.name}
            </button>
          ))}
        </motion.div>

        {/* Projects Grid */}
        <div className="projects-grid">
          <AnimatePresence mode="wait">
            {filteredProjects.map((project, index) => (
              <motion.div
                key={project.id}
                className="project-card card scroll-reveal"
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                onClick={() => setSelectedProject(project)}
              >
                <div className="project-image">
                  <img src={project.image} alt={project.title} />
                  <div className="project-overlay">
                    <FiExternalLink className="overlay-icon" />
                    <span>View Details</span>
                  </div>
                </div>
                <div className="project-content">
                  <h3 className="project-title">{project.title}</h3>
                  <p className="project-description">{project.description}</p>
                  <div className="project-tags">
                    {project.tags.map((tag, tagIndex) => (
                      <span key={tagIndex} className="project-tag">{tag}</span>
                    ))}
                  </div>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>

        {/* Project Modal */}
        <AnimatePresence>
          {selectedProject && (
            <motion.div
              className="modal-overlay"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setSelectedProject(null)}
            >
              <motion.div
                className="modal-content"
                initial={{ scale: 0.9, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                exit={{ scale: 0.9, opacity: 0 }}
                onClick={(e) => e.stopPropagation()}
              >
                <button
                  className="modal-close"
                  onClick={() => setSelectedProject(null)}
                >
                  <FiX />
                </button>
                <div className="modal-image">
                  <img src={selectedProject.image} alt={selectedProject.title} />
                </div>
                <div className="modal-body">
                  <h2 className="modal-title">{selectedProject.title}</h2>
                  <p className="modal-description">{selectedProject.fullDescription}</p>
                  <div className="modal-tags">
                    {selectedProject.tags.map((tag, index) => (
                      <span key={index} className="modal-tag">{tag}</span>
                    ))}
                  </div>
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Call to Action */}
        <motion.div
          className="projects-cta scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          <div className="cta-card card">
            <h3 className="cta-title">Want to see more?</h3>
            <p className="cta-text">
              Follow me on social media to see my latest creations and projects!
            </p>
            <div className="cta-buttons">
              <a href="https://instagram.com/bokamoso" target="_blank" rel="noopener noreferrer" className="btn-primary">
                Instagram
              </a>
              <a href="https://tiktok.com/@bokamoso" target="_blank" rel="noopener noreferrer" className="btn-primary">
                TikTok
              </a>
              <a href="https://facebook.com/bokasyarnmarket" target="_blank" rel="noopener noreferrer" className="btn-primary">
                Facebook
              </a>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default Projects;
