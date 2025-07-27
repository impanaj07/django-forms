# 📝 Django Feedback Form Project

This project is a simple web-based feedback/entry form built using **Django**. Over the past couple of sessions, I explored key Django form handling tools — including both **Form classes** and **ModelForms**, as well as moving from function-based views to **Class-Based Views (CBVs)** for better structure and reuse.

---

## ✅ What I Explored

### 🧾 Django Forms
- Creating basic forms with `forms.Form`
- Rendering custom form fields in templates
- Validating data with `form.is_valid()`
- Displaying errors and feedback messages

### 🗃️ ModelForms
- Connecting a form directly to a Django model
- Auto-generating fields based on database structure
- Simplifying save operations with `form.save()`

### 🧱 Class-Based Views (CBVs)
- Replacing function-based views with `FormView` and `TemplateView`
- Using `get_context_data()` and `form_valid()` for cleaner logic
- Adding custom logic in a modular way

---

## 🧠 Key Takeaways

- **ModelForms** significantly reduce boilerplate code when dealing with models.
- **Class-Based Views** improve reusability and separation of concerns.
- Django’s generic views like `FormView`, `CreateView`, and `UpdateView` make it easier to build CRUD interfaces quickly.

---

## 📁 Project Highlights

- A form for submitting user data (like name or review)
- Stored in a model using `ModelForm`
- Handled with a `FormView` CBV
- Redirects to a thank-you page after submission
- Uses templates for frontend rendering
---