import React, { useState } from 'react';
import { FiMail, FiPhone, FiMapPin, FiInstagram, FiSend, FiCheck } from 'react-icons/fi';
import { FaFacebook, FaTiktok, FaWhatsapp } from 'react-icons/fa';
import { motion } from 'framer-motion';
import emailjs from 'emailjs-com';
import './Contact.css';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });
  const [status, setStatus] = useState({ type: '', message: '' });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const contactInfo = [
    {
      icon: <FiMail />,
      title: 'Email',
      value: 'rainbow11272005@gmail.com',
      link: 'mailto:rainbow11272005@gmail.com'
    },
    {
      icon: <FiPhone />,
      title: 'Phone / WhatsApp',
      value: '079 320 0067',
      link: 'tel:+27793200067'
    },
    {
      icon: <FiMapPin />,
      title: 'Location',
      value: 'Midrand, South Africa',
      link: '#'
    }
  ];

  const socialLinks = [
    {
      icon: <FiInstagram />,
      name: 'Instagram',
      handle: '@bokamoso',
      link: 'https://instagram.com/bokamoso',
      color: '#E4405F'
    },
    {
      icon: <FaTiktok />,
      name: 'TikTok',
      handle: '@bokamoso',
      link: 'https://tiktok.com/@bokamoso',
      color: '#000000'
    },
    {
      icon: <FaFacebook />,
      name: 'Facebook',
      handle: 'Boka\'s Yarn Market',
      link: 'https://facebook.com/bokasyarnmarket',
      color: '#1877F2'
    },
    {
      icon: <FaWhatsapp />,
      name: 'WhatsApp',
      handle: '079 320 0067',
      link: 'https://wa.me/27793200067',
      color: '#25D366'
    }
  ];

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setStatus({ type: '', message: '' });

    // EmailJS configuration (you'll need to set up your own EmailJS account)
    // For now, this is a placeholder that simulates sending
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      // Uncomment and configure when you set up EmailJS:
      /*
      await emailjs.send(
        'YOUR_SERVICE_ID',
        'YOUR_TEMPLATE_ID',
        {
          from_name: formData.name,
          from_email: formData.email,
          subject: formData.subject,
          message: formData.message,
          to_email: 'rainbow11272005@gmail.com'
        },
        'YOUR_PUBLIC_KEY'
      );
      */

      setStatus({
        type: 'success',
        message: 'Thank you! Your message has been sent successfully. I\'ll get back to you soon!'
      });
      setFormData({ name: '', email: '', subject: '', message: '' });
    } catch (error) {
      setStatus({
        type: 'error',
        message: 'Oops! Something went wrong. Please try again or contact me directly via email.'
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <section id="contact" className="contact section">
      <div className="container">
        <motion.div
          className="section-header scroll-reveal"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="section-title">Get In Touch</h2>
          <p className="section-subtitle">
            Let's connect! I'm always open to discussing new opportunities, collaborations, or just having a chat.
          </p>
        </motion.div>

        <div className="contact-content">
          {/* Contact Info */}
          <motion.div
            className="contact-info scroll-reveal"
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <div className="info-card card">
              <h3 className="info-title gradient-text">Contact Information</h3>
              <p className="info-description">
                Feel free to reach out through any of these channels. I typically respond within 24 hours.
              </p>

              <div className="info-items">
                {contactInfo.map((item, index) => (
                  <a
                    key={index}
                    href={item.link}
                    className="info-item"
                    target={item.link.startsWith('http') ? '_blank' : '_self'}
                    rel="noopener noreferrer"
                  >
                    <div className="info-icon">{item.icon}</div>
                    <div className="info-content">
                      <h4 className="info-item-title">{item.title}</h4>
                      <p className="info-item-value">{item.value}</p>
                    </div>
                  </a>
                ))}
              </div>

              {/* Social Links */}
              <div className="social-section">
                <h4 className="social-title">Follow Me</h4>
                <div className="social-links">
                  {socialLinks.map((social, index) => (
                    <a
                      key={index}
                      href={social.link}
                      className="social-link"
                      target="_blank"
                      rel="noopener noreferrer"
                      style={{ '--social-color': social.color }}
                    >
                      <div className="social-icon">{social.icon}</div>
                      <div className="social-info">
                        <span className="social-name">{social.name}</span>
                        <span className="social-handle">{social.handle}</span>
                      </div>
                    </a>
                  ))}
                </div>
              </div>
            </div>
          </motion.div>

          {/* Contact Form */}
          <motion.div
            className="contact-form-wrapper scroll-reveal"
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <div className="form-card card">
              <h3 className="form-title">Send Me a Message</h3>
              <form onSubmit={handleSubmit} className="contact-form">
                <div className="form-group">
                  <label htmlFor="name" className="form-label">Your Name *</label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    className="form-input"
                    value={formData.name}
                    onChange={handleChange}
                    required
                    placeholder="John Doe"
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="email" className="form-label">Your Email *</label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    className="form-input"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    placeholder="john@example.com"
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="subject" className="form-label">Subject *</label>
                  <input
                    type="text"
                    id="subject"
                    name="subject"
                    className="form-input"
                    value={formData.subject}
                    onChange={handleChange}
                    required
                    placeholder="What's this about?"
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="message" className="form-label">Message *</label>
                  <textarea
                    id="message"
                    name="message"
                    className="form-textarea"
                    value={formData.message}
                    onChange={handleChange}
                    required
                    rows="6"
                    placeholder="Tell me about your project or inquiry..."
                  ></textarea>
                </div>

                {status.message && (
                  <div className={`form-status ${status.type}`}>
                    {status.type === 'success' ? <FiCheck /> : '⚠️'}
                    <span>{status.message}</span>
                  </div>
                )}

                <button
                  type="submit"
                  className="btn-primary form-submit"
                  disabled={isSubmitting}
                >
                  {isSubmitting ? (
                    <>
                      <div className="loading-spinner"></div>
                      Sending...
                    </>
                  ) : (
                    <>
                      <FiSend /> Send Message
                    </>
                  )}
                </button>
              </form>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default Contact;
