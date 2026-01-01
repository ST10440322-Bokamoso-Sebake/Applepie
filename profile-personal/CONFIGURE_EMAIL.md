# EmailJS Configuration Guide - Step by Step

Follow these steps to configure EmailJS for your contact form.

## ⚡ Quick Start Checklist

- [ ] Step 1: Create EmailJS Account
- [ ] Step 2: Add Email Service (Gmail)
- [ ] Step 3: Create Email Template
- [ ] Step 4: Get Public Key
- [ ] Step 5: Update .env.local file
- [ ] Step 6: Test the contact form

---

## 📋 Detailed Steps

### Step 1: Create EmailJS Account (2 minutes)

1. **Go to EmailJS Website**
   - Visit: https://www.emailjs.com/
   - Click **"Sign Up"** button (top right)

2. **Sign Up Options**
   - You can sign up with Google (fastest)
   - Or use email and password

3. **Verify Your Email**
   - Check your email inbox
   - Click the verification link
   - You'll be redirected to the dashboard

✅ **You're done with Step 1 when:** You can see the EmailJS dashboard

---

### Step 2: Add Email Service (3 minutes)

1. **Navigate to Email Services**
   - In the left sidebar, click **"Email Services"**
   - Or go to: https://dashboard.emailjs.com/admin/integration

2. **Add New Service**
   - Click the **"Add New Service"** button
   - You'll see different email providers

3. **Choose Gmail (Recommended)**
   - Click on **"Gmail"** icon
   - Click **"Connect Account"** button

4. **Connect Your Gmail**
   - Sign in with: **rainbow11272005@gmail.com**
   - Allow EmailJS to access your Gmail
   - Click **"Allow"** on the permissions screen

5. **Copy Your Service ID**
   - After connecting, you'll see a **Service ID**
   - It looks like: `service_abc123` or `service_xyz789`
   - **COPY THIS** - you'll need it in Step 5
   - You can also see it later by clicking on the service name

✅ **You're done with Step 2 when:** You have a Service ID copied

---

### Step 3: Create Email Template (5 minutes)

1. **Navigate to Email Templates**
   - In the left sidebar, click **"Email Templates"**
   - Or go to: https://dashboard.emailjs.com/admin/template

2. **Create New Template**
   - Click **"Create New Template"** button
   - Choose **"Blank Template"** or start with a basic template

3. **Configure Template Settings**

   **Template Name:**
   ```
   Portfolio Contact Form
   ```

   **Subject Line:**
   ```
   New Contact Form Message from {{from_name}}
   ```

   **Email Content:**
   ```
   You have received a new message from your portfolio contact form.

   Name: {{from_name}}
   Email: {{from_email}}
   Subject: {{subject}}

   Message:
   {{message}}

   ---
   This message was sent from your portfolio website.
   ```

   **Important Notes:**
   - The variables `{{from_name}}`, `{{from_email}}`, `{{subject}}`, and `{{message}}` must match exactly
   - These will be replaced with actual form data when the form is submitted
   - You can customize the email content however you like

4. **Save the Template**
   - Click **"Save"** button at the bottom
   - Your template is now created

5. **Copy Your Template ID**
   - After saving, you'll see a **Template ID**
   - It looks like: `template_abc123` or `template_xyz789`
   - **COPY THIS** - you'll need it in Step 5

✅ **You're done with Step 3 when:** You have a Template ID copied

---

### Step 4: Get Your Public Key (1 minute)

1. **Navigate to Account Settings**
   - Click on your profile/account icon (top right)
   - Click **"Account"** or **"General"**
   - Or go to: https://dashboard.emailjs.com/admin/account/general

2. **Find Your Public Key**
   - Scroll down to find **"API Keys"** section
   - You'll see **"Public Key"** (also called API Key)
   - It's a long string like: `abcdefghijklmnopqrstuvwxyz123456`
   - **COPY THIS** - you'll need it in Step 5

✅ **You're done with Step 4 when:** You have your Public Key copied

---

### Step 5: Update .env.local File (2 minutes)

1. **Open .env.local File**
   - In your project root folder, open `.env.local`
   - It should currently have placeholder values

2. **Replace the Placeholder Values**

   Find this in your `.env.local` file:
   ```env
   REACT_APP_EMAILJS_SERVICE_ID=your_service_id_here
   REACT_APP_EMAILJS_TEMPLATE_ID=your_template_id_here
   REACT_APP_EMAILJS_PUBLIC_KEY=your_public_key_here
   ```

   Replace with your actual values:
   ```env
   REACT_APP_EMAILJS_SERVICE_ID=service_abc123
   REACT_APP_EMAILJS_TEMPLATE_ID=template_xyz789
   REACT_APP_EMAILJS_PUBLIC_KEY=abcdefghijklmnopqrstuvwxyz123456
   ```

   **Example (with fake values):**
   ```env
   REACT_APP_EMAILJS_SERVICE_ID=service_8k7m2n1
   REACT_APP_EMAILJS_TEMPLATE_ID=template_4p5q6r
   REACT_APP_EMAILJS_PUBLIC_KEY=abc123xyz789def456ghi012jkl345mno678
   ```

3. **Save the File**
   - Save the `.env.local` file
   - Make sure there are no extra spaces or quotes around the values

✅ **You're done with Step 5 when:** .env.local has your actual credentials

---

### Step 6: Test the Contact Form (2 minutes)

1. **Restart Your Development Server**
   - If your server is running, stop it (Ctrl+C)
   - Start it again: `npm start`
   - **Important:** React needs to reload environment variables

2. **Open Your Website**
   - Go to: http://localhost:3000
   - Navigate to the Contact section

3. **Fill Out the Form**
   - Enter your name
   - Enter your email
   - Enter a test subject
   - Enter a test message
   - Click **"Send Message"**

4. **Check Your Email**
   - Go to: rainbow11272005@gmail.com
   - Check your inbox (and spam folder if needed)
   - You should receive the email within a few seconds!

✅ **Success!** If you received the email, everything is working!

---

## 🎯 What You Need to Copy

Here's a checklist of what to copy from EmailJS:

- [ ] **Service ID** - From Step 2 (Email Services section)
  - Looks like: `service_abc123`
  
- [ ] **Template ID** - From Step 3 (Email Templates section)
  - Looks like: `template_xyz789`
  
- [ ] **Public Key** - From Step 4 (Account → General section)
  - Looks like: `abcdefghijklmnopqrstuvwxyz123456`

---

## 🔍 Where to Find Your Credentials Later

If you need to find your credentials again:

- **Service ID**: Dashboard → Email Services → Click on your service name
- **Template ID**: Dashboard → Email Templates → Click on your template name
- **Public Key**: Dashboard → Account → General → API Keys section

---

## ❌ Troubleshooting

### "Email service is not configured" Error

- Make sure you updated `.env.local` with actual values (not placeholders)
- Make sure you restarted your development server after updating `.env.local`
- Check that there are no extra spaces in your `.env.local` file
- Verify all three values are filled in

### Email Not Sending

- Check browser console (F12) for error messages
- Verify all three IDs/keys in `.env.local` are correct
- Make sure your EmailJS account is verified
- Check that your Gmail connection is still active in EmailJS

### Template Variables Not Working

- Make sure variable names match exactly: `{{from_name}}`, `{{from_email}}`, `{{subject}}`, `{{message}}`
- Variables are case-sensitive
- Check your EmailJS template editor to verify variable names

### Still Having Issues?

1. Double-check all three credentials are correct in `.env.local`
2. Make sure you restarted the server after updating `.env.local`
3. Check EmailJS dashboard to ensure service is connected
4. Try disconnecting and reconnecting Gmail in EmailJS
5. Check EmailJS dashboard for any error messages

---

## 💡 Tips

- The free plan allows 200 emails per month (perfect for a portfolio!)
- Your `.env.local` file is already in `.gitignore` - it won't be committed to Git
- You can test the form multiple times to make sure it's working
- Keep your credentials safe and never share them publicly

---

## ✅ Final Checklist

Before you consider setup complete:

- [ ] Created EmailJS account
- [ ] Added Gmail service
- [ ] Created email template
- [ ] Got Public Key
- [ ] Updated `.env.local` with all three values
- [ ] Restarted development server
- [ ] Tested contact form
- [ ] Received test email in your inbox

**Congratulations! Your contact form is now fully configured! 🎉**

