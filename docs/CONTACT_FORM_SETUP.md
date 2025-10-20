# 📧 Contact Form Setup Guide

## ✅ **EmailJS Integration Complete!**

Your contact form is now ready to send real emails! Here's how to complete the setup:

## 🚀 **Step-by-Step Setup**

### **1. Create EmailJS Account**
1. Go to [EmailJS.com](https://www.emailjs.com/)
2. Sign up for a free account
3. Verify your email address

### **2. Set Up Email Service**
1. In your EmailJS dashboard, go to **"Email Services"**
2. Click **"Add New Service"**
3. Choose your email provider:
   - **Gmail** (recommended for personal use)
   - **Outlook**
   - **Yahoo**
   - Or any other provider
4. Follow the setup instructions for your chosen provider
5. **Copy your Service ID** (you'll need this)

### **3. Create Email Template**
1. Go to **"Email Templates"** in your dashboard
2. Click **"Create New Template"**
3. Use this template content:

```
Subject: New Contact Form Message: {{subject}}

From: {{from_name}} ({{from_email}})

Message:
{{message}}

---
This message was sent from your portfolio contact form.
```

4. **Copy your Template ID** (you'll need this)

### **4. Get Your Public Key**
1. Go to **"Account"** → **"General"**
2. **Copy your Public Key**

### **5. Update Your Code**
Replace these placeholders in `/website/script.js`:

```javascript
// Line 97: Replace 'YOUR_PUBLIC_KEY'
emailjs.init('YOUR_PUBLIC_KEY');

// Line 131: Replace 'YOUR_SERVICE_ID' and 'YOUR_TEMPLATE_ID'
emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', {
```

**Example:**
```javascript
emailjs.init('user_abc123def456');
emailjs.send('service_gmail', 'template_contact', {
```

## 🎯 **Alternative Options**

### **Option 2: Formspree (Even Easier)**
If you prefer a simpler solution:

1. Go to [Formspree.io](https://formspree.io/)
2. Sign up and create a new form
3. Get your form endpoint URL
4. Replace the EmailJS code with:

```javascript
// Replace the EmailJS code with this:
fetch('https://formspree.io/f/YOUR_FORM_ID', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        name: name,
        email: email,
        subject: subject,
        message: message
    })
})
.then(response => response.json())
.then(data => {
    showNotification('Thank you for your message! I\'ll get back to you soon.', 'success');
    contactForm.reset();
})
.catch(error => {
    showNotification('Sorry, there was an error. Please try again.', 'error');
});
```

### **Option 3: Netlify Forms (If using Netlify)**
If you deploy to Netlify:

1. Add `netlify` attribute to your form:
```html
<form id="contact-form" netlify netlify-honeypot="bot-field">
    <input type="hidden" name="bot-field" />
    <!-- rest of your form -->
</form>
```

2. Remove the JavaScript form handling (Netlify handles it automatically)

## 🔧 **Features Included**

Your contact form now has:
- ✅ **Real email sending** via EmailJS
- ✅ **Form validation** (required fields, email format)
- ✅ **Loading states** (button shows "Sending..." while processing)
- ✅ **Success/error notifications**
- ✅ **Form reset** after successful submission
- ✅ **Professional error handling**

## 🧪 **Testing**

1. **Complete the EmailJS setup** (steps 1-5 above)
2. **Test locally** at `http://localhost:8000/website/`
3. **Fill out the contact form**
4. **Check your email** for the message
5. **Verify the notification** appears correctly

## 📱 **Mobile Responsive**

The form works perfectly on:
- ✅ Desktop computers
- ✅ Tablets
- ✅ Mobile phones
- ✅ All screen sizes

## 🚀 **Deployment Ready**

Once you complete the EmailJS setup, your contact form will work on:
- ✅ GitHub Pages
- ✅ Netlify
- ✅ Vercel
- ✅ Any static hosting service

## 💡 **Pro Tips**

1. **Test thoroughly** before going live
2. **Check spam folder** for test emails
3. **Consider adding a honeypot field** for spam protection
4. **Monitor your EmailJS usage** (free tier has limits)
5. **Keep your keys secure** (don't commit them to public repos)

## 🆘 **Troubleshooting**

**Form not sending?**
- Check browser console for errors
- Verify your EmailJS keys are correct
- Ensure your email service is properly configured

**Emails going to spam?**
- Add SPF/DKIM records to your domain
- Use a professional email address
- Avoid spam trigger words in templates

**Need help?**
- Check EmailJS documentation
- Contact EmailJS support
- Review the browser console for error messages

---

**🎉 Once setup is complete, your contact form will send real emails directly to grantgardner455@gmail.com!**
