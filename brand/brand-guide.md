# Austral Waves Brand Guidelines

## Logo

The Austral Waves logo represents the convergence of sound waves and the cyclical nature of radio broadcasting. The design consists of concentric circles with intersecting elements, symbolizing the spread of sound waves and the connection between music and listeners.

### Logo Versions

1. **Primary Logo (`logo.svg`)**
   - Full-size vector logo
   - Dimensions: 500x500px
   - Available in both dark and light themes
   - Includes metadata and responsive theme switching

2. **Favicon (`favicon.svg`)**
   - Simplified version for small displays
   - Dimensions: 32x32px
   - Optimized for browser tabs and bookmarks
   - Responsive theme support

### Color Palette

**Dark Theme:**
- Background: #000000 (Pure Black)
- Logo Stroke: #FFFFFF (Pure White)
- Accent: #888888 (Subtle Gray)

**Light Theme:**
- Background: #FFFFFF (Pure White)
- Logo Stroke: #000000 (Pure Black)
- Accent: #666666 (Dark Gray)

### Typography

- Font Family: Inter
- Fallback Stack: -apple-system, BlinkMacSystemFont, sans-serif
- Logo Text: Uppercase with 0.1em letter spacing

### Usage Guidelines

1. **Spacing**
   - Maintain minimum clear space around logo equal to the width of the outer circle's stroke
   - Do not compress or stretch the logo
   - Keep aspect ratio 1:1 when scaling

2. **Modifications**
   - Do not alter the circle proportions
   - Do not change the stroke widths
   - Do not add fills to the circles
   - Do not rotate individual elements

3. **Themes**
   - Use appropriate theme version based on background
   - Dark theme on dark backgrounds
   - Light theme on light backgrounds
   - Maintain contrast ratio of at least 4.5:1

4. **Minimum Size**
   - Web: 40px width minimum
   - Print: 0.5 inches / 12.7mm minimum
   - Use favicon version for smaller applications

### Animation Guidelines

When animating the logo:
- Keep rotations smooth and subtle
- Use transition duration of 0.3s for hover effects
- Maintain stroke width transitions between 2px and 3px
- Center all rotations around the middle point

### File Formats

- SVG: Primary format for web use
- PNG: Available in 16px, 32px, 64px, 128px, 256px, and 512px
- PDF: Vector format for print use

## Implementation

```html
<!-- Logo Implementation Example -->
<a href="/" class="logo">
    <svg viewBox="0 0 100 100" class="logo-circles">
        <!-- Logo SVG content -->
    </svg>
    Austral Waves
</a>
```

```css
/* Logo Styling Example */
.logo {
    display: flex;
    align-items: center;
    gap: 1rem;
    font-size: 1.5rem;
    font-weight: 300;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
```

## Contact

For questions about brand usage or to request additional formats:
- Email: brand@australwaves.com
- Website: www.australwaves.com 