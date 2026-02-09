# Testing Guide - Flight Booking Enhancements

## Quick Start

### 1. Apply Database Changes
```bash
cd "C:\Users\rajju\OneDrive\Pictures\Django project"
myvenv\Scripts\activate
cd myProject
python manage.py migrate
python manage.py runserver
```

### 2. Open Browser
Navigate to: http://127.0.0.1:8000/

## Test Checklist

### ✅ Test 1: Multiple Passengers Feature

**Steps:**
1. Go to Flights page
2. Click "Book Now" on any flight
3. Look for "Number of Passengers" field at the top of the form
4. Try changing the number from 1 to 3
5. Watch the "Total Price" update automatically

**Expected Results:**
- ✓ Number input appears with min=1, max=available seats
- ✓ Price shows "Price per Passenger: $X"
- ✓ Price shows "Total Price (3 passengers): $Y"
- ✓ Total = Per Passenger × Number of Passengers
- ✓ Cannot exceed available seats

**Example:**
```
If flight costs $500 and you select 3 passengers:
- Price per Passenger: $500
- Total Price (3 passengers): $1500
```

### ✅ Test 2: Simplified Phone Number

**Steps:**
1. On the booking form, scroll to phone number field
2. Check that there's NO country code dropdown
3. Enter a phone number directly (e.g., "9841234567")
4. Submit the form

**Expected Results:**
- ✓ Single text input field (no dropdown)
- ✓ Placeholder shows example number
- ✓ Can enter number directly
- ✓ Number saves correctly

**Before:** [+977 ▼] [Phone Number]
**After:**  [Phone Number (e.g., 9841234567)]

### ✅ Test 3: Page Load Animations

**Steps:**
1. Open homepage (http://127.0.0.1:8000/)
2. Watch as page loads
3. Refresh page (F5) to see again
4. Navigate to Flights page
5. Navigate to booking page

**Expected Results:**
- ✓ Navigation slides in from left/right
- ✓ Cards fade in and slide up
- ✓ Elements appear smoothly, not instantly
- ✓ Staggered animation (not all at once)

### ✅ Test 4: Hover Animations

**Test on Homepage:**
1. Hover over flight cards
2. Hover over package cards
3. Hover over deal cards
4. Hover over navigation links
5. Hover over buttons

**Expected Results:**
- ✓ Cards lift up and scale slightly
- ✓ Shadow becomes more prominent
- ✓ Smooth transition (not jumpy)
- ✓ Nav links get underline animation
- ✓ Buttons lift with shadow

**Test on Booking Page:**
1. Hover over seat selections
2. Hover over class options (Economy/Business/First)
3. Hover over detail items (Date, Aircraft, etc.)
4. Hover over price display

**Expected Results:**
- ✓ Seats scale and rotate slightly
- ✓ Class cards lift up
- ✓ Detail items slide and highlight
- ✓ Price display lifts with shadow

### ✅ Test 5: Form Interactions

**Steps:**
1. Click on any input field
2. Type something
3. Tab to next field
4. Change passenger count
5. Select seat class

**Expected Results:**
- ✓ Input lifts slightly on focus
- ✓ Border color changes to red/primary
- ✓ Shadow appears around input
- ✓ Smooth transition
- ✓ Price updates when passenger count changes

### ✅ Test 6: Scroll Animations

**Steps:**
1. Go to homepage
2. Scroll down slowly
3. Watch elements appear as you scroll
4. Scroll back up
5. Try on Flights page

**Expected Results:**
- ✓ Elements fade in as they enter viewport
- ✓ Smooth appearance (not instant)
- ✓ Navbar changes style on scroll
- ✓ Smooth scroll behavior

### ✅ Test 7: Spacing & Layout

**Visual Inspection:**
1. Check spacing between sections
2. Check padding inside cards
3. Check form field spacing
4. Check button sizes
5. Check overall layout

**Expected Results:**
- ✓ More breathing room between elements
- ✓ Consistent spacing throughout
- ✓ Larger, more comfortable inputs
- ✓ Better visual hierarchy
- ✓ Modern, clean appearance

### ✅ Test 8: Complete Booking Flow

**Full Test:**
1. Select a flight
2. Click "Book Now"
3. Enter passenger count: 2
4. Fill in name and email
5. Enter phone: "1234567890"
6. Select nationality
7. Choose seat class
8. Select a seat
9. Submit booking

**Expected Results:**
- ✓ Form validates correctly
- ✓ Price shows for 2 passengers
- ✓ Phone saves without country code
- ✓ Booking succeeds
- ✓ Confirmation shows correct details
- ✓ Seat availability decreases by 2

### ✅ Test 9: Responsive Design

**Steps:**
1. Resize browser window
2. Test on mobile size (< 768px)
3. Test on tablet size (768-1024px)
4. Test on desktop (> 1024px)

**Expected Results:**
- ✓ Layout adapts to screen size
- ✓ Animations still work
- ✓ Forms remain usable
- ✓ No horizontal scroll
- ✓ Touch-friendly on mobile

### ✅ Test 10: Browser Compatibility

**Test in:**
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

**Expected Results:**
- ✓ Animations work in all browsers
- ✓ Layout consistent
- ✓ No console errors
- ✓ Smooth performance

## Common Issues & Solutions

### Issue 1: Animations Not Working
**Solution:**
- Clear browser cache (Ctrl + F5)
- Check if JavaScript is enabled
- Open browser console for errors

### Issue 2: Price Not Updating
**Solution:**
- Check browser console for JavaScript errors
- Ensure num_passengers input has id="num_passengers"
- Verify updateTotalPrice() function exists

### Issue 3: Migration Error
**Solution:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue 4: CSS Not Loading
**Solution:**
```bash
python manage.py collectstatic
```
Then hard refresh browser (Ctrl + F5)

### Issue 5: Phone Field Still Has Country Code
**Solution:**
- Clear browser cache
- Check book_flight.html was updated correctly
- Verify you're looking at the right page

## Performance Testing

### Check Animation Performance:
1. Open Chrome DevTools (F12)
2. Go to Performance tab
3. Record while scrolling/hovering
4. Check for 60fps

**Expected:**
- ✓ Smooth 60fps animations
- ✓ No layout thrashing
- ✓ GPU acceleration active

### Check Load Time:
1. Open Network tab in DevTools
2. Refresh page
3. Check load time

**Expected:**
- ✓ CSS loads quickly
- ✓ No blocking resources
- ✓ Fast initial render

## Accessibility Testing

### Keyboard Navigation:
1. Use Tab key to navigate
2. Use Enter to submit
3. Use Space for checkboxes

**Expected:**
- ✓ All elements reachable
- ✓ Focus visible
- ✓ Logical tab order

### Screen Reader:
1. Test with screen reader if available
2. Check form labels
3. Check button text

**Expected:**
- ✓ All labels present
- ✓ Meaningful button text
- ✓ Proper ARIA attributes

## Success Criteria

All tests pass when:
- ✅ Multiple passengers can be booked
- ✅ Phone number works without country code
- ✅ Animations are smooth and professional
- ✅ Spacing looks modern and clean
- ✅ No console errors
- ✅ Responsive on all devices
- ✅ Works in all major browsers
- ✅ Performance is good (60fps)
- ✅ Accessible via keyboard
- ✅ Complete booking flow works

## Reporting Issues

If you find any issues:
1. Note the browser and version
2. Describe what you expected
3. Describe what actually happened
4. Include any console errors
5. Include screenshots if possible

## Next Steps After Testing

Once all tests pass:
1. ✅ Deploy to production
2. ✅ Monitor user feedback
3. ✅ Check analytics for booking completion rate
4. ✅ Gather user feedback on new features
5. ✅ Plan next enhancements
