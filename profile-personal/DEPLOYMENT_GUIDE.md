# Deployment Guide for Profile Project

## 🚀 Quick Deploy to Vercel (Easiest Method)

### Step 1: Go to Vercel
1. Visit [https://vercel.com](https://vercel.com)
2. Sign in with your **GitHub account** (the same one you used to push the code)

### Step 2: Import Your Project
1. Click **"Add New..."** → **"Project"**
2. Find and select your repository: **`ST10440322-Bokamoso-Sebake/Applepie`**
3. Click **"Import"**

### Step 3: Configure Project Settings
**IMPORTANT:** Since your project is in a subfolder, configure these settings:

- **Root Directory:** Click "Edit" and set it to: `profile-personal`
- **Framework Preset:** Create React App (should auto-detect)
- **Build Command:** `npm run build` (should be auto-filled)
- **Output Directory:** `build` (should be auto-filled)

### Step 4: Add Environment Variables (Optional - Only if you want contact form to work)
If you've set up EmailJS and have a `.env.local` file, add these in Vercel:

1. Click **"Environment Variables"** section
2. Add these three variables:
   - `REACT_APP_EMAILJS_SERVICE_ID` = (your service ID)
   - `REACT_APP_EMAILJS_TEMPLATE_ID` = (your template ID)
   - `REACT_APP_EMAILJS_PUBLIC_KEY` = (your public key)

**Note:** If you don't have EmailJS set up yet, you can skip this step and add it later. The site will deploy fine, but the contact form won't send emails.

### Step 5: Deploy!
1. Click **"Deploy"**
2. Wait 1-2 minutes for the build to complete
3. Your site will be live at: `https://your-project-name.vercel.app`

### Step 6: Custom Domain (Optional)
- Vercel gives you a free domain automatically
- You can add a custom domain later in Project Settings → Domains

---

## 🌐 Alternative: Deploy to Netlify

### Method 1: Connect GitHub (Recommended)
1. Go to [https://netlify.com](https://netlify.com)
2. Sign in with GitHub
3. Click **"Add new site"** → **"Import an existing project"**
4. Select your GitHub repository: **`ST10440322-Bokamoso-Sebake/Applepie`**
5. Configure:
   - **Base directory:** `profile-personal`
   - **Build command:** `npm run build`
   - **Publish directory:** `profile-personal/build`
6. Add environment variables (if using EmailJS) in Site Settings → Environment Variables
7. Click **"Deploy site"**

### Method 2: Drag & Drop
1. Build your project: `npm run build`
2. Go to [https://app.netlify.com/drop](https://app.netlify.com/drop)
3. Drag the `build` folder onto the page
4. Your site is live!

---

## 📄 Deploy to GitHub Pages

1. Install gh-pages:
   ```bash
   npm install --save-dev gh-pages
   ```

2. Add to `package.json`:
   ```json
   "homepage": "https://ST10440322-Bokamoso-Sebake.github.io/Applepie",
   "scripts": {
     "predeploy": "npm run build",
     "deploy": "gh-pages -d build"
   }
   ```

3. Deploy:
   ```bash
   npm run deploy
   ```

**Note:** GitHub Pages requires the project to be in the root, so you may need to adjust the structure.

---

## ✅ After Deployment Checklist

- [ ] Test your site on the live URL
- [ ] Check all links work correctly
- [ ] Test the contact form (if EmailJS is configured)
- [ ] Test on mobile devices
- [ ] Verify all images load correctly
- [ ] Check that PDF downloads work (resume, CV, cover letter)

---

## 🔧 Troubleshooting

### Build Fails
- Make sure `package.json` is in the `profile-personal` folder
- Check that all dependencies are installed: `npm install`
- Verify the build works locally: `npm run build`

### Images Not Loading
- Make sure image paths are correct
- Check that images are in the `public` or `src/assets` folder

### Contact Form Not Working
- Verify EmailJS environment variables are set in Vercel/Netlify
- Check the EmailJS setup guide: `EMAILJS_SETUP.md`

---

## 🎉 You're Done!

Your portfolio is now live! Share the URL with potential employers, clients, and on your social media.

