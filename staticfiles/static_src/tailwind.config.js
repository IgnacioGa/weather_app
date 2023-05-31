/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',
        '../../apps/**/templates/**/*.html',
        '../../apps/**/components/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {},
        colors: {
            WHITE: '#FFFFFF',
            BLACK: '#000000',
            BLUE_LIGHT: '#DDF5F7',
            BLUE_MEDIUM: '#C0D9E5',
            BLUE_DARK: '#44679F',
            BLUE_DARKER: '#3B577D',
            GRAY_LIGHT: '#f3f4f6',
            GRAY_MEDIUM: '#9ca3af',
            GREEN_LIGHT: '#bbf7d0',
            GREEN_MEDIUM: '#22c55e',
            GREEN_DARK: '#14532d',
            RED_LIGHT: '#fecaca',
            RED_MEDIUM: '#fca5a5',
            RED_DARK: '#7f1d1d',
        }
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
    safelist: [
        'float-message-error',
        'float-message-success',
        'show',
        'loading',
        'htmx-request',
        'city',
        'city-active',
        'border-BLUE_DARKER'
    ]
}
