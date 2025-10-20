# 🔒 Security & Rate Limiting Guide

## ✅ **Enhanced Security Features Added!**

Your contact form now has multiple layers of protection:

### **🛡️ Security Features Implemented:**

#### **1. Content Filtering:**
- ✅ **XSS Protection** - Blocks script tags and JavaScript
- ✅ **HTML Injection Prevention** - Filters out HTML tags
- ✅ **URL Filtering** - Prevents malicious links (optional)
- ✅ **Event Handler Blocking** - Stops onclick, onload, etc.

#### **2. Rate Limiting:**
- ✅ **Client-side Rate Limiting** - Max 3 submissions per 5 minutes
- ✅ **Automatic Reset** - Counter resets after time window
- ✅ **User-friendly Messages** - Clear feedback on limits

#### **3. EmailJS Built-in Protection:**
- ✅ **Server-side Rate Limiting** - 200 emails/month (free tier)
- ✅ **Domain Restrictions** - Can whitelist specific domains
- ✅ **Spam Filtering** - Built-in spam detection
- ✅ **HTTPS Enforcement** - Required for production

## 📊 **Rate Limits Summary:**

### **EmailJS Limits:**
- **Free Tier**: 200 emails/month
- **Paid Tiers**: Up to 10,000 emails/month
- **Per-minute**: Automatic throttling

### **Your Custom Limits:**
- **Per User**: 3 submissions per 5 minutes
- **Content**: Blocks suspicious patterns
- **Validation**: Required fields + email format

## 🔧 **Additional Security Recommendations:**

### **1. EmailJS Dashboard Settings:**
1. **Go to your EmailJS dashboard**
2. **Navigate to "Account" → "General"**
3. **Set up domain restrictions:**
   - Add your production domain (e.g., `runn3rman.github.io`)
   - Remove `localhost` for production
4. **Enable additional security features**

### **2. Email Template Security:**
Your email template should be simple and safe:
```
Subject: Portfolio Contact: {{subject}}

From: {{from_name}} ({{from_email}})

Message: {{message}}

---
Sent from your portfolio contact form.
```

### **3. Production Deployment:**
- ✅ **Use HTTPS** (GitHub Pages provides this automatically)
- ✅ **Remove localhost** from allowed domains in EmailJS
- ✅ **Test thoroughly** before going live

## 🚨 **What to Monitor:**

### **EmailJS Dashboard:**
- **Usage Statistics** - Monitor email volume
- **Failed Attempts** - Check for abuse patterns
- **Domain Activity** - Verify legitimate traffic

### **Your Email:**
- **Spam Folder** - Check for legitimate emails
- **Unusual Patterns** - Watch for automated submissions
- **Content Quality** - Review message content

## ⚙️ **Customization Options:**

### **Adjust Rate Limits:**
In `script.js`, modify these values:
```javascript
const timeWindow = 5 * 60 * 1000; // 5 minutes (change as needed)
const maxSubmissions = 3; // Max submissions per window
```

### **Modify Content Filtering:**
In the `containsSuspiciousContent` function:
```javascript
const suspiciousPatterns = [
    /<script/i,           // Block scripts
    /javascript:/i,       // Block javascript: URLs
    /on\w+\s*=/i,        // Block event handlers
    /http[s]?:\/\/[^\s]+/i, // Block URLs (remove if you want to allow links)
    /[<>]/g              // Block HTML tags
];
```

### **Allow Links (Optional):**
If you want to allow URLs in messages, remove this line:
```javascript
/http[s]?:\/\/[^\s]+/i, // Remove this line to allow URLs
```

## 🔍 **Testing Your Security:**

### **Test Rate Limiting:**
1. Submit 3 forms quickly
2. Try to submit a 4th form
3. Should see "Please wait a moment" message

### **Test Content Filtering:**
Try submitting forms with:
- `<script>alert('test')</script>`
- `javascript:alert('test')`
- `<iframe src="evil.com"></iframe>`
- Should be blocked with appropriate message

### **Test Email Delivery:**
1. Submit a legitimate form
2. Check your email (including spam folder)
3. Verify all fields are included correctly

## 🆘 **Troubleshooting:**

### **Form Not Sending:**
- Check browser console for errors
- Verify EmailJS keys are correct
- Ensure domain is whitelisted in EmailJS

### **Rate Limiting Too Strict:**
- Increase `maxSubmissions` or `timeWindow`
- Consider removing client-side limits if EmailJS limits are sufficient

### **Legitimate Messages Blocked:**
- Review `suspiciousPatterns` array
- Remove overly restrictive patterns
- Test with real message content

## 📈 **Scaling Considerations:**

### **If You Get Popular:**
- **Upgrade EmailJS plan** for higher limits
- **Add server-side validation** for better security
- **Implement CAPTCHA** for additional protection
- **Add IP-based rate limiting**

### **Enterprise Features:**
- **Custom email templates**
- **Advanced analytics**
- **Webhook notifications**
- **API access for custom integrations**

## 🎯 **Current Security Level: GOOD**

Your contact form now has:
- ✅ **Multi-layer protection**
- ✅ **Rate limiting**
- ✅ **Content filtering**
- ✅ **Professional error handling**
- ✅ **User-friendly feedback**

**This is suitable for a personal portfolio and will protect against most common attacks while maintaining a good user experience.**

---

**🔒 Your contact form is now secure and ready for production use!**
