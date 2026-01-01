/**
 * EmailJS Configuration Checker
 * Run this script to verify your EmailJS configuration
 * 
 * Usage: node check-email-config.js
 */

const fs = require('fs');
const path = require('path');

console.log('🔍 Checking EmailJS Configuration...\n');

const envPath = path.join(__dirname, '.env.local');

// Check if .env.local exists
if (!fs.existsSync(envPath)) {
  console.log('❌ .env.local file not found!');
  console.log('   Please create a .env.local file in the root directory.');
  console.log('   See CONFIGURE_EMAIL.md for instructions.\n');
  process.exit(1);
}

// Read .env.local file
const envContent = fs.readFileSync(envPath, 'utf8');
const lines = envContent.split('\n');

let serviceId = null;
let templateId = null;
let publicKey = null;

// Parse environment variables
lines.forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const [key, ...valueParts] = trimmed.split('=');
    const value = valueParts.join('=').trim();
    
    if (key === 'REACT_APP_EMAILJS_SERVICE_ID') {
      serviceId = value;
    } else if (key === 'REACT_APP_EMAILJS_TEMPLATE_ID') {
      templateId = value;
    } else if (key === 'REACT_APP_EMAILJS_PUBLIC_KEY') {
      publicKey = value;
    }
  }
});

console.log('📋 Current Configuration:\n');

// Check Service ID
if (!serviceId || serviceId === 'your_service_id_here') {
  console.log('❌ REACT_APP_EMAILJS_SERVICE_ID: Not configured');
  console.log('   Expected format: service_abc123');
} else {
  console.log(`✅ REACT_APP_EMAILJS_SERVICE_ID: ${serviceId}`);
}

// Check Template ID
if (!templateId || templateId === 'your_template_id_here') {
  console.log('❌ REACT_APP_EMAILJS_TEMPLATE_ID: Not configured');
  console.log('   Expected format: template_abc123');
} else {
  console.log(`✅ REACT_APP_EMAILJS_TEMPLATE_ID: ${templateId}`);
}

// Check Public Key
if (!publicKey || publicKey === 'your_public_key_here') {
  console.log('❌ REACT_APP_EMAILJS_PUBLIC_KEY: Not configured');
  console.log('   Expected format: abc123xyz789... (long string)');
} else {
  const maskedKey = publicKey.length > 20 
    ? publicKey.substring(0, 10) + '...' + publicKey.substring(publicKey.length - 10)
    : '***';
  console.log(`✅ REACT_APP_EMAILJS_PUBLIC_KEY: ${maskedKey}`);
}

console.log('\n');

// Final check
const allConfigured = serviceId && templateId && publicKey &&
  serviceId !== 'your_service_id_here' &&
  templateId !== 'your_template_id_here' &&
  publicKey !== 'your_public_key_here';

if (allConfigured) {
  console.log('✅ All EmailJS credentials are configured!');
  console.log('   Make sure to restart your development server if it\'s running.');
  console.log('   Then test your contact form to verify everything works.\n');
} else {
  console.log('❌ EmailJS is not fully configured yet.');
  console.log('   Please follow the instructions in CONFIGURE_EMAIL.md');
  console.log('   to set up your EmailJS account and update .env.local\n');
  process.exit(1);
}

