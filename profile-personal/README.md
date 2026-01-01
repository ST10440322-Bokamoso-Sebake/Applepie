# Bokamoso Sebake - Interactive Portfolio

A modern, interactive portfolio website for Bokamoso Sebake, showcasing her journey as the founder of Boka's Yarn Market and Computer Science student.

## 🌟 Features

- **Modern Design**: Beautiful purple-themed design with smooth animations
- **Dark/Light Mode**: Toggle between dark and light themes with persistent preference
- **Fully Responsive**: Optimized for all devices (desktop, tablet, mobile)
- **Interactive Sections**:
  - Hero section with animated introduction
  - About section with detailed background
  - Achievements timeline
  - Skills showcase with progress bars
  - Project gallery with filtering
  - Vision and goals section
  - Contact form with validation
- **Downloadable Documents**: Resume, CV, and Cover Letter downloads
- **Social Media Integration**: Links to Instagram, TikTok, Facebook, and WhatsApp
- **Smooth Animations**: Framer Motion animations throughout
- **SEO Optimized**: Proper meta tags and semantic HTML

## 🚀 Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Start Development Server**
   ```bash
   npm start
   ```
   The site will open at `http://localhost:3000`

3. **Build for Production**
   ```bash
   npm run build
   ```

## 📝 Customization Guide

### 1. Personal Information

Update your personal information in the following files:

- **Hero Section** (`src/components/Hero.jsx`): Update name, title, and introduction
- **About Section** (`src/components/About.jsx`): Update your story and background
- **Contact Section** (`src/components/Contact.jsx`): Update email, phone, and social links
- **Footer** (`src/components/Footer.jsx`): Update contact information

### 2. Replace Placeholder Content

#### Profile Photo
- Add your professional photo to `public/` folder
- Update the image path in `src/components/Hero.jsx`

#### Documents
Replace the placeholder PDFs in the `public/` folder:
- `public/resume.pdf` - Your resume
- `public/cv.pdf` - Your CV
- `public/cover-letter.pdf` - Your cover letter

#### Project Images
- Add your project images to `public/images/` folder
- Update image URLs in `src/components/Projects.jsx`

### 3. Social Media Links

Update social media links in:
- `src/components/Hero.jsx`
- `src/components/Contact.jsx`
- `src/components/Footer.jsx`

Replace placeholder links with your actual profiles:
```javascript
// Example:
{ link: 'https://instagram.com/your_username' }
```

### 4. Contact Form Setup

To enable the contact form to send emails:

1. Sign up for [EmailJS](https://www.emailjs.com/)
2. Create an email service and template
3. Get your Service ID, Template ID, and Public Key
4. Update `src/components/Contact.jsx`:

```javascript
await emailjs.send(
  'YOUR_SERVICE_ID',      // Replace with your Service ID
  'YOUR_TEMPLATE_ID',     // Replace with your Template ID
  {
    from_name: formData.name,
    from_email: formData.email,
    subject: formData.subject,
    message: formData.message,
    to_email: 'your-email@example.com'
  },
  'YOUR_PUBLIC_KEY'       // Replace with your Public Key
);
```

### 5. Color Customization

To change the color scheme, update CSS variables in `src/index.css`:

```css
:root {
  --primary: #8B5CF6;      /* Main purple color */
  --secondary: #A78BFA;    /* Light purple */
  --accent: #C084FC;       /* Soft purple */
  /* ... other colors */
}
```

### 6. Content Updates

#### Skills
Update your skills in `src/components/Skills.jsx`:
```javascript
skills: [
  { name: 'Your Skill', level: 85 },
  // Add more skills
]
```

#### Achievements
Update achievements in `src/components/Achievements.jsx`

#### Projects
Update projects in `src/components/Projects.jsx`:
```javascript
{
  title: 'Project Name',
  category: 'crochet', // or 'business', 'tech'
  description: 'Short description',
  fullDescription: 'Detailed description',
  image: 'path/to/image.jpg',
  tags: ['Tag1', 'Tag2'],
  link: 'project-url'
}
```

## 🎨 Theme Customization

The site supports both light and dark themes. The theme preference is saved in localStorage and persists across sessions.

To modify theme colors, edit `src/index.css`:
- Light theme colors are in `:root`
- Dark theme colors are in `[data-theme="dark"]`

## 📱 Responsive Design

The site is fully responsive with breakpoints at:
- Desktop: 1200px+
- Tablet: 768px - 1199px
- Mobile: < 768px

## 🔧 Technologies Used

- **React** - UI library
- **Framer Motion** - Animations
- **React Icons** - Icon library
- **EmailJS** - Contact form functionality
- **CSS3** - Styling with CSS variables
- **HTML5** - Semantic markup

## 📦 Project Structure

```
profile-personal/
├── public/
│   ├── index.html
│   ├── resume.pdf
│   ├── cv.pdf
│   └── cover-letter.pdf
├── src/
│   ├── components/
│   │   ├── Header.jsx/css
│   │   ├── Hero.jsx/css
│   │   ├── About.jsx/css
│   │   ├── Achievements.jsx/css
│   │   ├── Skills.jsx/css
│   │   ├── Projects.jsx/css
│   │   ├── Vision.jsx/css
│   │   ├── Contact.jsx/css
│   │   └── Footer.jsx/css
│   ├── styles/
│   │   ├── themes.css
│   │   └── animations.css
│   ├── App.jsx
│   ├── App.css
│   ├── index.js
│   └── index.css
├── package.json
└── README.md
```

## 🚀 Deployment

### Deploy to Vercel (Recommended)

1. Push your code to GitHub
2. Go to [Vercel](https://vercel.com)
3. Import your repository
4. Deploy!

### Deploy to Netlify

1. Build the project: `npm run build`
2. Drag and drop the `build` folder to [Netlify](https://netlify.com)

### Deploy to GitHub Pages

1. Install gh-pages: `npm install --save-dev gh-pages`
2. Add to package.json:
   ```json
   "homepage": "https://yourusername.github.io/repository-name",
   "scripts": {
     "predeploy": "npm run build",
     "deploy": "gh-pages -d build"
   }
   ```
3. Deploy: `npm run deploy`

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Support

For questions or support, contact:
- Email: rainbow11272005@gmail.com
- WhatsApp: 079 320 0067

## 🎉 Acknowledgments

- Design inspiration from modern portfolio websites
- Icons from React Icons
- Fonts from Google Fonts (Inter & Playfair Display)

---

**Made with ❤️ by Bokamoso Sebake**
