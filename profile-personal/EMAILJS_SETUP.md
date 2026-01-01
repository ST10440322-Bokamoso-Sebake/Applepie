# EmailJS Setup Instructions

To enable email functionality for your contact form, you need to set up an EmailJS account and configure it.

## Step 1: Create an EmailJS Account

1. Go to [https://www.emailjs.com/](https://www.emailjs.com/)
2. Sign up for a free account (you get 200 emails/month on the free plan)
3. Verify your email address

## Step 2: Add an Email Service

1. Once logged in, go to **Email Services** in the dashboard
2. Click **Add New Service**
3. Choose your email provider (Gmail is recommended and easiest)
4. Connect your email account (rainbow11272005@gmail.com)
5. Copy the **Service ID** (you'll need this later)

## Step 3: Create an Email Template

1. Go to **Email Templates** in the dashboard
2. Click **Create New Template**
3. Use this template structure:

**Template Name:** Contact Form Template

**Subject:** New Contact Form Message from {{from_name}}

**Content:**
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

4. Click **Save**
5. Copy the **Template ID** (you'll need this later)

## Step 4: Get Your Public Key

1. Go to **Account** → **General** in the dashboard
2. Find your **Public Key** (also called API Key)
3. Copy it (you'll need this later)

## Step 5: Configure Your Project

1. Open the `.env.local` file in the root of your project
2. Replace the placeholder values with your actual credentials:

```
REACT_APP_EMAILJS_SERVICE_ID=your_actual_service_id
REACT_APP_EMAILJS_TEMPLATE_ID=your_actual_template_id
REACT_APP_EMAILJS_PUBLIC_KEY=your_actual_public_key
```

**Important:** 
- Never commit the `.env.local` file to Git (it's already in .gitignore)
- The file should be in the root directory, not in the src folder
- After updating `.env.local`, restart your development server (stop and run `npm start` again)

## Step 6: Test It Out

1. Restart your development server if it's running
2. Go to your contact form
3. Fill out and submit a test message
4. Check your email (rainbow11272005@gmail.com) - you should receive the message!

## Troubleshooting

- **"Email service is not configured"** - Make sure you've updated `.env.local` with your actual credentials and restarted the server
- **Emails not sending** - Check the browser console for errors, verify your EmailJS credentials are correct
- **Template variables not working** - Make sure the variable names in your template match exactly: `{{from_name}}`, `{{from_email}}`, `{{subject}}`, `{{message}}`

## Free Plan Limits

The free EmailJS plan includes:
- 200 emails per month
- Gmail, Outlook, and other major email providers
- Perfect for a personal portfolio!

If you need more, you can upgrade to a paid plan later.

