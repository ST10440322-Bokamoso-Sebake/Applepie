# Setup Guide - Getting Started

## ⚠️ Important: Node.js Installation Required

Your interactive portfolio is now ready, but you need to install Node.js to run it.

## 📥 Step 1: Install Node.js

### Windows Installation:

1. **Download Node.js**
   - Go to: https://nodejs.org/
   - Download the **LTS (Long Term Support)** version
   - Choose the Windows Installer (.msi) for your system (64-bit recommended)

2. **Install Node.js**
   - Run the downloaded installer
   - Follow the installation wizard
   - ✅ Make sure to check "Automatically install necessary tools" option
   - Click "Install" and wait for completion
   - Restart your computer after installation

3. **Verify Installation**
   - Open a new Command Prompt or PowerShell window
   - Run these commands:
   ```bash
   node --version
   npm --version
   ```
   - You should see version numbers (e.g., v18.x.x and 9.x.x)

## 🚀 Step 2: Install Project Dependencies

Once Node.js is installed:

1. **Open Terminal in Project Folder**
   - Open Command Prompt or PowerShell
   - Navigate to your project folder:
   ```bash
   cd "C:\Users\Esther\Desktop\Persoanl github projects\Personal-Projects27\profile-personal"
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```
   - This will install all required packages (React, Framer Motion, etc.)
   - Wait for the installation to complete (may take 2-5 minutes)

## ▶️ Step 3: Start the Development Server

After installation is complete:

```bash
npm start
```

- Your browser will automatically open at `http://localhost:3000`
- The site will reload automatically when you make changes
- Press `Ctrl + C` in the terminal to stop the server

## 🎨 Step 4: Customize Your Portfolio

### Quick Customization Checklist:

#### 1. Replace Placeholder PDFs
- [ ] Add your resume to `public/resume.pdf`
- [ ] Add your CV to `public/cv.pdf`
- [ ] Add your cover letter to `public/cover-letter.pdf`

#### 2. Add Your Photo
- [ ] Add your professional photo to `public/` folder (e.g., `profile-photo.jpg`)
- [ ] Update the image path in `src/components/Hero.jsx` (line ~95)

#### 3. Update Social Media Links
Files to update:
- [ ] `src/components/Hero.jsx`
- [ ] `src/components/Contact.jsx`
- [ ] `src/components/Footer.jsx`

Replace placeholder URLs with your actual profiles:
```javascript
// Example:
'https://instagram.com/bokamoso' → 'https://instagram.com/your_actual_username'
```

#### 4. Update Contact Information
In `src/components/Contact.jsx`, verify:
- [ ] Email address
- [ ] Phone number
- [ ] WhatsApp link

#### 5. Customize Content
- [ ] Update skills in `src/components/Skills.jsx`
- [ ] Update achievements in `src/components/Achievements.jsx`
- [ ] Update projects in `src/components/Projects.jsx`
- [ ] Review and update all text content

#### 6. Add Project Images
- [ ] Create folder: `public/images/projects/`
- [ ] Add your project images
- [ ] Update image paths in `src/components/Projects.jsx`

## 📧 Step 5: Setup Contact Form (Optional)

To enable email functionality:

1. **Sign up for EmailJS**
   - Go to: https://www.emailjs.com/
   - Create a free account
   - Add an email service (Gmail, Outlook, etc.)
   - Create an email template

2. **Get Your Credentials**
   - Service ID
   - Template ID
   - Public Key

3. **Update Contact Form**
   - Open `src/components/Contact.jsx`
   - Find the commented section (around line 75)
   - Uncomment and add your credentials:
   ```javascript
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
   ```

## 🌐 Step 6: Deploy Your Portfolio

### Option 1: Vercel (Recommended - Free & Easy)

1. **Create GitHub Repository**
   - Go to: https://github.com/new
   - Create a new repository
   - Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Deploy to Vercel**
   - Go to: https://vercel.com
   - Sign up with GitHub
   - Click "New Project"
   - Import your repository
   - Click "Deploy"
   - Your site will be live in minutes!

### Option 2: Netlify (Also Free & Easy)

1. **Build Your Project**
   ```bash
   npm run build
   ```

2. **Deploy to Netlify**
   - Go to: https://app.netlify.com/drop
   - Drag and drop your `build` folder
   - Your site is live!

### Option 3: GitHub Pages

1. **Install gh-pages**
   ```bash
   npm install --save-dev gh-pages
   ```

2. **Update package.json**
   Add these lines:
   ```json
   "homepage": "https://yourusername.github.io/repository-name",
   "scripts": {
     "predeploy": "npm run build",
     "deploy": "gh-pages -d build"
   }
   ```

3. **Deploy**
   ```bash
   npm run deploy
   ```

## 🎯 Quick Start Commands

```bash
# Install dependencies (first time only)
npm install

# Start development server
npm start

# Build for production
npm run build

# Test production build locally
npm install -g serve
serve -s build
```

## 🆘 Troubleshooting

### Issue: "npm is not recognized"
**Solution**: Node.js is not installed or not in PATH. Reinstall Node.js and restart your computer.

### Issue: Port 3000 is already in use
**Solution**: 
- Close other applications using port 3000
- Or use a different port: `PORT=3001 npm start`

### Issue: Module not found errors
**Solution**: 
```bash
rm -rf node_modules package-lock.json
npm install
```

### Issue: Build fails
**Solution**: 
- Check for syntax errors in your code
- Make sure all imports are correct
- Run `npm install` again

## 📞 Need Help?

If you encounter any issues:
1. Check the error message carefully
2. Search for the error on Google or Stack Overflow
3. Contact me:
   - Email: rainbow11272005@gmail.com
   - WhatsApp: 079 320 0067

## ✅ Final Checklist

Before deploying:
- [ ] Node.js installed and working
- [ ] All dependencies installed (`npm install`)
- [ ] Site runs locally (`npm start`)
- [ ] All placeholder content replaced
- [ ] Social media links updated
- [ ] Contact information verified
- [ ] PDFs replaced with actual documents
- [ ] Photos added
- [ ] Tested on mobile and desktop
- [ ] Contact form tested (if enabled)
- [ ] Ready to deploy!

---

**Good luck with your portfolio! 🚀**
