import React from 'react';
import { FiStar } from 'react-icons/fi';
import { motion } from 'framer-motion';
import './Testimonials.css';

const Testimonials = () => {
  const testimonials = [
    {
      id: 1,
      name: 'Sarah Johnson',
      role: 'Fashion Enthusiast',
      image: 'https://via.placeholder.com/100/8B5CF6/FFFFFF?text=SJ',
      rating: 5,
      text: 'The crochet pieces from Boka\'s Yarn Market are absolutely stunning! The attention to detail and quality is unmatched. I\'ve received so many compliments on my custom cardigan.',
      date: 'March 2024'
    },
    {
      id: 2,
      name: 'Michael Chen',
      role: 'Interior Designer',
      image: 'https://via.placeholder.com/100/A78BFA/FFFFFF?text=MC',
      rating: 5,
      text: 'I ordered custom home décor pieces and they transformed my living space! Bokamoso\'s creativity and professionalism are exceptional. Highly recommend!',
      date: 'February 2024'
    },
    {
      id: 3,
      name: 'Thandi Mthembu',
      role: 'Business Owner',
      image: 'https://via.placeholder.com/100/C084FC/FFFFFF?text=TM',
      rating: 5,
      text: 'Working with Bokamoso has been a pleasure. Her entrepreneurial spirit and dedication to quality are inspiring. The products are beautiful and unique!',
      date: 'January 2024'
    },
    {
      id: 4,
      name: 'Emma Williams',
      role: 'Fashion Blogger',
      image: 'https://via.placeholder.com/100/DDD6FE/8B5CF6?text=EW',
      rating: 5,
      text: 'As a fashion blogger, I\'m always looking for unique pieces. Boka\'s Yarn Market delivers every time! The craftsmanship is incredible and the designs are so trendy.',
      date: 'December 2023'
    },
    {
      id: 5,
      name: 'David Nkosi',
      role: 'Gift Shopper',
      image: 'https://via.placeholder.com/100/8B5CF6/FFFFFF?text=DN',
      rating: 5,
      text: 'I bought a custom crochet bag as a gift and it was a huge hit! The quality exceeded my expectations. Will definitely be ordering again.',
      date: 'November 2023'
    },
    {
      id: 6,
      name: 'Lisa Anderson',
      role: 'Art Collector',
      image: 'https://via.placeholder.com/100/A78BFA/FFFFFF?text=LA',
      rating: 5,
      text: 'The wall hangings I purchased are true works of art! Bokamoso\'s talent shines through in every stitch. These pieces add so much character to my home.',
      date: 'October 2023'
    }
  ];

  return (
    <section id="testimonials" className="testimonials section">
      <div className="container">
        <motion.div
          className="section-header scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="section-title">What Customers Say</h2>
          <p className="section-subtitle">
            Real feedback from satisfied customers who love handmade quality
          </p>
        </motion.div>

        {/* Stats */}
        <div className="testimonials-stats">
          <motion.div
            className="stat-card scroll-reveal"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.1 }}
          >
            <div className="stat-icon">⭐</div>
            <h3 className="stat-value gradient-text">5.0</h3>
            <p className="stat-label">Average Rating</p>
          </motion.div>

          <motion.div
            className="stat-card scroll-reveal"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <div className="stat-icon">💬</div>
            <h3 className="stat-value gradient-text">100+</h3>
            <p className="stat-label">Happy Reviews</p>
          </motion.div>

          <motion.div
            className="stat-card scroll-reveal"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.3 }}
          >
            <div className="stat-icon">🎯</div>
            <h3 className="stat-value gradient-text">98%</h3>
            <p className="stat-label">Satisfaction Rate</p>
          </motion.div>
        </div>

        {/* Testimonials Grid */}
        <div className="testimonials-grid">
          {testimonials.map((testimonial, index) => (
            <motion.div
              key={testimonial.id}
              className="testimonial-card card scroll-reveal"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
            >
              <div className="testimonial-header">
                <img
                  src={testimonial.image}
                  alt={testimonial.name}
                  className="testimonial-avatar"
                />
                <div className="testimonial-info">
                  <h4 className="testimonial-name">{testimonial.name}</h4>
                  <p className="testimonial-role">{testimonial.role}</p>
                </div>
              </div>

              <div className="testimonial-rating">
                {[...Array(testimonial.rating)].map((_, i) => (
                  <FiStar key={i} className="star-icon filled" />
                ))}
              </div>

              <p className="testimonial-text">"{testimonial.text}"</p>

              <p className="testimonial-date">{testimonial.date}</p>
            </motion.div>
          ))}
        </div>

        {/* Call to Action */}
        <motion.div
          className="testimonials-cta scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          <div className="cta-content">
            <h3 className="cta-title">Want to be our next happy customer?</h3>
            <p className="cta-description">
              Join hundreds of satisfied customers who love our handmade creations
            </p>
            <a href="#contact" className="btn-primary">Get Started</a>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default Testimonials;
