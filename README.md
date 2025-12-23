# Marins PlayLab - Official Website
Marins PlayLab is an independent space for exploring STEM and more through interactive, open projects, visuals, experiments, and discoveries.
This is a curiosity driven passion project in a very early phase, with a simple goal: make learning feel simple, clear, and fun. The focus is on short educational posts, science news, visual explanations, and small projects you can try yourself, such as simulations that let you explore ideas instead of only reading about them.
Contributions are welcome, especially from people with deeper knowledge in specific topics.
Over time, the aim is to grow the community and this space into a wider collection of topics across science, space, technology, engineering, math, and the broader world of curiosity, including history and other fields that connect to how we understand the universe.

It is built using HTML, CSS, Bootstrap, and reusable header and footer templates to make it easy to extend and maintain.

This project is licensed under the MIT License. See the LICENSE file for details.

## Project Structure
```
.
├── .htaccess
├── 404.html
├── about.html
├── index.html
├── templates/
│   ├── header.html
│   └── footer.html
├── css/
│   └── style.css
├── js/
│   └── include.js
└── images/
    ├── favicon.jpg
    ├── gallery/
    ├── logo.jpg
    └── socials/
        ├── bluesky.svg
        ├── github.svg
        └── x.svg
```

## Run Locally on macOS
1. Open Terminal and navigate to the project folder:
```bash
cd /path/to/website
```

2. Start a local server:
```bash
python3 -m http.server
```

3. Open your browser and go to:
`http://localhost:8000`

### Stop the Local Server
Press `Ctrl + C` in the Terminal where the server is running.

## Notes
- Do not open `index.html` directly using `file://`  
- A local server is required for header/footer loading (they are fetched from `templates/`)  
- The website is mobile-friendly and built with responsive design in mind
- Code style: CSS/JS use brace-on-new-line formatting

## Open Source and Transparency
The website and its projects are published openly on https://github.com/marinsplaylab-org/ so people can learn from them, reuse them, and improve them. The site is early stage, so updates will arrive gradually.

## Privacy
No ads. No aggressive tracking. Only essential services are used to run the site and projects. If a third party service is involved, their policies apply and they handle their own data.

## Tech Used
- HTML  
- CSS  
- Bootstrap 5  
- JavaScript

## Contributing / Feedback
This is an open-source project. At the moment, we are **not accepting code pull requests**.

You can help with:
- Issues: bug reports, feature requests, scientific corrections, attribution fixes
- PRs: documentation only (no code changes)

Code PRs may be closed without review. If you want to propose a code change, please open an issue first.

## Future Plans
- Add more interactive educational projects  
- Expand research resources  
- Improve user interface and accessibility  
- Continuously update with new content and features
