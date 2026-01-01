import React from 'react';
import { FiCheck, FiShoppingBag, FiHeart, FiStar } from 'react-icons/fi';
import { motion } from 'framer-motion';
import './Services.css';

const Services = () => {
  const services = [
    {
      icon: <FiShoppingBag />,
      title: 'Custom Clothing',
      description: 'Handmade crochet clothing tailored to your style and measurements',
      features: [
        'Personalized designs',
        'Premium yarn quality',
        'Perfect fit guarantee',
        'Unique patterns',
        'Color customization'
      ],
      popular: false
    },
    {
      icon: <FiHeart />,
      title: 'Accessories',
      description: 'Trendy crochet accessories to complement any outfit',
      features: [
        'Bags & purses',
        'Hats & beanies',
        'Scarves & shawls',
        'Jewelry pieces',
        'Custom requests'
      ],
      popular: true
    },
    {
      icon: <FiStar />,
      title: 'Home Décor',
      description: 'Beautiful handcrafted pieces to transform your living space',
      features: [
        'Blankets & throws',
        'Cushion covers',
        'Wall hangings',
        'Table runners',
        'Plant holders'
      ],
      popular: false
    }
  ];

  const process = [
    {
      step: '01',
      title: 'Consultation',
      description: 'Share your vision and requirements with us'
    },
    {
      step: '02',
      title: 'Design',
      description: 'We create a custom design based on your preferences'
    },
    {
      step: '03',
      title: 'Creation',
      description: 'Handcrafted with care and attention to detail'
    },
    {
      step: '04',
      title: 'Delivery',
      description: 'Your unique piece delivered with love'
    }
  ];

  return (
    <section id="services" className="services section">
      <div className="container">
        <motion.div
          className="section-header scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="section-title">Services & Offerings</h2>
          <p className="section-subtitle">
            Handmade crochet creations crafted with passion and precision
          </p>
        </motion.div>

        {/* Services Grid */}
        <div className="services-grid">
          {services.map((service, index) => (
            <motion.div
              key={index}
              className={`service-card card scroll-reveal ${service.popular ? 'popular' : ''}`}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
            >
              {service.popular && (
                <div className="popular-badge">
                  <span>Most Popular</span>
                </div>
              )}

              <div className="service-icon">{service.icon}</div>
              <h3 className="service-title">{service.title}</h3>
              <p className="service-description">{service.description}</p>

              <ul className="service-features">
                {service.features.map((feature, featureIndex) => (
                  <li key={featureIndex} className="feature-item">
                    <FiCheck className="check-icon" />
                    <span>{feature}</span>
                  </li>
                ))}
              </ul>

              <a href="#contact" className="service-button btn-secondary">
                Get Quote
              </a>
            </motion.div>
          ))}
        </div>

        {/* Process Section */}
        <motion.div
          className="process-section scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          <h3 className="process-title">How It Works</h3>
          <p className="process-subtitle">
            From concept to creation, we make the process simple and enjoyable
          </p>

          <div className="process-steps">
            {process.map((item, index) => (
              <motion.div
                key={index}
                className="process-step"
                initial={{ opacity: 0, x: -30 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
              >
                <div className="step-number">{item.step}</div>
                <div className="step-content">
                  <h4 className="step-title">{item.title}</h4>
                  <p className="step-description">{item.description}</p>
                </div>
                {index < process.length - 1 && (
                  <div className="step-connector"></div>
                )}
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* Why Choose Us */}
        <motion.div
          className="why-choose-us scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          <div className="why-card card">
            <h3 className="why-title gradient-text">Why Choose Boka's Yarn Market?</h3>
            <div className="why-grid">
              <div className="why-item">
                <div className="why-icon">🎨</div>
                <h4>Unique Designs</h4>
                <p>Every piece is one-of-a-kind, designed specifically for you</p>
              </div>
              <div className="why-item">
                <div className="why-icon">💎</div>
                <h4>Premium Quality</h4>
                <p>We use only the finest yarns and materials</p>
              </div>
              <div className="why-item">
                <div className="why-icon">❤️</div>
                <h4>Made with Love</h4>
                <p>Each stitch is crafted with care and passion</p>
              </div>
              <div className="why-item">
                <div className="why-icon">⚡</div>
                <h4>Fast Turnaround</h4>
                <p>Efficient creation without compromising quality</p>
              </div>
              <div className="why-item">
                <div className="why-icon">🌟</div>
                <h4>Customer Focused</h4>
                <p>Your satisfaction is our top priority</p>
              </div>
              <div className="why-item">
                <div className="why-icon">♻️</div>
                <h4>Sustainable</h4>
                <p>Eco-friendly materials and practices</p>
              </div>
            </div>
          </div>
        </motion.div>

        {/* CTA */}
        <motion.div
          className="services-cta scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.5 }}
        >
          <h3 className="cta-heading">Ready to Create Something Special?</h3>
          <p className="cta-text">
            Let's bring your vision to life with handmade crochet artistry
          </p>
          <a href="#contact" className="btn-primary">Start Your Project</a>
        </motion.div>
      </div>
    </section>
  );
};

export default Services;
