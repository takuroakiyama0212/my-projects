from flask import Flask, send_file, render_template_string
import os
import shutil

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dual Subs - Learn Languages While Watching</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        :root {
            --purple: #8b5cf6;
            --pink: #ec4899;
            --blue: #3b82f6;
            --cyan: #06b6d4;
        }
        
        body {
            font-family: 'Inter', 'Noto Sans JP', sans-serif;
            background: #030014;
            color: #fff;
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        .bg-grid {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(139, 92, 246, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(139, 92, 246, 0.03) 1px, transparent 1px);
            background-size: 60px 60px;
            z-index: 0;
        }
        
        .glow-orb {
            position: fixed;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.5;
            z-index: 0;
            animation: float 8s ease-in-out infinite;
        }
        
        .orb-1 {
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, var(--purple) 0%, transparent 70%);
            top: -200px;
            right: -100px;
            animation-delay: 0s;
        }
        
        .orb-2 {
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, var(--pink) 0%, transparent 70%);
            bottom: -150px;
            left: -100px;
            animation-delay: -4s;
        }
        
        .orb-3 {
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, var(--blue) 0%, transparent 70%);
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            animation-delay: -2s;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-30px) scale(1.05); }
        }
        
        .particles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            overflow: hidden;
        }
        
        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255,255,255,0.5);
            border-radius: 50%;
            animation: rise 10s linear infinite;
        }
        
        @keyframes rise {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) scale(1); opacity: 0; }
        }
        
        .content {
            position: relative;
            z-index: 1;
        }
        
        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
            background: rgba(3, 0, 20, 0.8);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        
        .nav-logo {
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 800;
            font-size: 1.4rem;
        }
        
        .nav-logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--purple), var(--pink));
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            font-weight: 900;
        }
        
        .nav-links {
            display: flex;
            gap: 30px;
        }
        
        .nav-links a {
            color: rgba(255,255,255,0.7);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: #fff;
        }
        
        .hero {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 120px 20px 80px;
        }
        
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: rgba(139, 92, 246, 0.15);
            border: 1px solid rgba(139, 92, 246, 0.3);
            border-radius: 50px;
            font-size: 0.85rem;
            color: #c4b5fd;
            margin-bottom: 30px;
            animation: fadeInUp 0.8s ease-out;
        }
        
        .badge::before {
            content: '✨';
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .hero-title {
            font-size: clamp(3rem, 8vw, 6rem);
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 24px;
            animation: fadeInUp 0.8s ease-out 0.1s both;
        }
        
        .hero-title .gradient {
            background: linear-gradient(135deg, #fff 0%, var(--purple) 50%, var(--pink) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-size: 200% 200%;
            animation: gradient 5s ease infinite;
        }
        
        @keyframes gradient {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            color: rgba(255,255,255,0.6);
            max-width: 600px;
            margin: 0 auto 50px;
            line-height: 1.7;
            animation: fadeInUp 0.8s ease-out 0.2s both;
        }
        
        .cta-group {
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
            justify-content: center;
            animation: fadeInUp 0.8s ease-out 0.3s both;
        }
        
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 16px 32px;
            border-radius: 14px;
            font-size: 1rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s ease;
            cursor: pointer;
            border: none;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, var(--purple), var(--pink));
            color: white;
            box-shadow: 0 0 40px rgba(139, 92, 246, 0.4);
            position: relative;
            overflow: hidden;
        }
        
        .btn-primary::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }
        
        .btn-primary:hover::before {
            left: 100%;
        }
        
        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 50px rgba(139, 92, 246, 0.5);
        }
        
        .btn-secondary {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: white;
        }
        
        .btn-secondary:hover {
            background: rgba(255,255,255,0.1);
            border-color: rgba(255,255,255,0.2);
        }
        
        .demo-container {
            margin-top: 80px;
            perspective: 1000px;
            animation: fadeInUp 0.8s ease-out 0.4s both;
        }
        
        .demo-window {
            background: linear-gradient(145deg, #1a1a2e 0%, #0f0f1a 100%);
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            overflow: visible;
            width: 90%;
            max-width: 700px;
            min-width: 400px;
            margin: 0 auto;
            box-shadow: 
                0 50px 100px rgba(0,0,0,0.5),
                0 0 0 1px rgba(255,255,255,0.05) inset,
                0 0 80px rgba(139, 92, 246, 0.2);
            transform: rotateX(5deg);
            transition: transform 0.5s ease;
        }
        
        .demo-window:hover {
            transform: rotateX(0deg) scale(1.02);
        }
        
        .demo-bar {
            padding: 12px 16px;
            background: rgba(255,255,255,0.03);
            border-bottom: 1px solid rgba(255,255,255,0.05);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .demo-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        
        .demo-dot.red { background: #ff5f57; }
        .demo-dot.yellow { background: #ffbd2e; }
        .demo-dot.green { background: #28ca42; }
        
        .demo-content {
            aspect-ratio: 16/9;
            background: linear-gradient(180deg, #0a0a15 0%, #050510 100%);
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: visible;
            min-height: 200px;
        }
        
        .demo-play {
            width: 80px;
            height: 80px;
            background: rgba(255,255,255,0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
        }
        
        .demo-subs {
            position: absolute;
            bottom: 20px;
            left: 0;
            right: 0;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }
        
        .demo-sub {
            padding: 8px 16px;
            background: rgba(0,0,0,0.85);
            border-radius: 6px;
            margin: 4px 0;
            font-weight: 600;
            font-size: 14px;
            backdrop-filter: blur(10px);
            animation: subtitlePulse 3s ease-in-out infinite;
            writing-mode: horizontal-tb !important;
            white-space: nowrap;
            display: inline-block;
            max-width: 90%;
        }
        
        .demo-sub.ko { 
            color: #60a5fa;
            border-left: 3px solid #60a5fa;
            animation-delay: 0s;
        }
        .demo-sub.ja { 
            color: #fbbf24;
            border-left: 3px solid #fbbf24;
            animation-delay: 0.2s;
        }
        
        @keyframes subtitlePulse {
            0%, 100% { opacity: 0.9; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.02); }
        }
        
        .section {
            padding: 120px 40px;
            position: relative;
        }
        
        .section-header {
            text-align: center;
            margin-bottom: 80px;
        }
        
        .section-title {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 20px;
        }
        
        .section-title .gradient {
            background: linear-gradient(135deg, var(--cyan), var(--purple), var(--pink));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .section-desc {
            color: rgba(255,255,255,0.5);
            font-size: 1.1rem;
            max-width: 500px;
            margin: 0 auto;
        }
        
        .langs-showcase {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-bottom: 60px;
        }
        
        .lang-card {
            padding: 20px 40px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            font-size: 1.5rem;
            font-weight: 700;
            transition: all 0.3s ease;
            cursor: default;
        }
        
        .lang-card:hover {
            transform: translateY(-5px);
            border-color: var(--purple);
            box-shadow: 0 20px 40px rgba(139, 92, 246, 0.2);
        }
        
        .lang-card.en { color: #fff; }
        .lang-card.ja { color: #fbbf24; }
        .lang-card.ko { color: #60a5fa; }
        .lang-card.zh { color: #f472b6; }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .feature-card {
            background: linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 24px;
            padding: 40px;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, var(--purple), var(--pink));
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        .feature-card:hover {
            transform: translateY(-8px);
            border-color: rgba(139, 92, 246, 0.3);
            box-shadow: 0 30px 60px rgba(0,0,0,0.3);
        }
        
        .feature-card:hover::before {
            opacity: 1;
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 24px;
            display: inline-block;
            animation: bounce 2s ease-in-out infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
        
        .feature-card h3 {
            font-size: 1.4rem;
            margin-bottom: 12px;
        }
        
        .feature-card p {
            color: rgba(255,255,255,0.5);
            line-height: 1.7;
        }
        
        .steps-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: wrap;
            max-width: 1000px;
            margin: 0 auto;
        }
        
        .step-card {
            flex: 1;
            min-width: 200px;
            max-width: 220px;
            text-align: center;
        }
        
        .step-num {
            width: 70px;
            height: 70px;
            background: linear-gradient(135deg, var(--purple), var(--pink));
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            font-weight: 900;
            margin: 0 auto 20px;
            box-shadow: 0 10px 30px rgba(139, 92, 246, 0.3);
        }
        
        .step-card h3 {
            font-size: 1.2rem;
            margin-bottom: 10px;
        }
        
        .step-card p {
            color: rgba(255,255,255,0.5);
            font-size: 0.95rem;
            line-height: 1.6;
        }
        
        .final-cta {
            text-align: center;
            padding: 100px 40px;
            background: linear-gradient(180deg, transparent, rgba(139, 92, 246, 0.1));
        }
        
        .final-cta h2 {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 20px;
        }
        
        .final-cta p {
            color: rgba(255,255,255,0.5);
            margin-bottom: 40px;
        }
        
        footer {
            padding: 40px;
            text-align: center;
            color: rgba(255,255,255,0.3);
            border-top: 1px solid rgba(255,255,255,0.05);
        }
        
        @media (max-width: 768px) {
            nav { padding: 15px 20px; }
            .nav-links { display: none; }
            .hero { padding: 100px 20px 60px; }
            .hero-title { font-size: 2.5rem; }
            .section { padding: 80px 20px; }
            .section-title { font-size: 2rem; }
        }
    </style>
</head>
<body>
    <div class="bg-grid"></div>
    <div class="glow-orb orb-1"></div>
    <div class="glow-orb orb-2"></div>
    <div class="glow-orb orb-3"></div>
    
    <div class="particles">
        <script>
            for(let i = 0; i < 30; i++) {
                const p = document.createElement('div');
                p.className = 'particle';
                p.style.left = Math.random() * 100 + '%';
                p.style.animationDelay = Math.random() * 10 + 's';
                p.style.animationDuration = (8 + Math.random() * 6) + 's';
                document.querySelector('.particles').appendChild(p);
            }
        </script>
    </div>
    
    <div class="content">
        <nav>
            <div class="nav-logo">
                <div class="nav-logo-icon">DS</div>
                <span>Dual Subs</span>
            </div>
            <div class="nav-links">
                <a href="#features">Features</a>
                <a href="#languages">Languages</a>
                <a href="#install">Install</a>
            </div>
        </nav>
        
        <section class="hero">
            <div class="badge">New Version Available</div>
            <h1 class="hero-title">
                Learn Languages<br>
                <span class="gradient">While You Watch</span>
            </h1>
            <p class="hero-subtitle">
                The ultimate Chrome extension for language learners. 
                Watch YouTube & Netflix with dual subtitles in any language combination.
            </p>
            <div class="cta-group">
                <a href="/download" class="btn btn-primary">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
                    Download Extension
                </a>
                <a href="#features" class="btn btn-secondary">Learn More</a>
            </div>
            
            <div class="demo-container">
                <div class="demo-window">
                    <div class="demo-bar">
                        <div class="demo-dot red"></div>
                        <div class="demo-dot yellow"></div>
                        <div class="demo-dot green"></div>
                    </div>
                    <div class="demo-content">
                        <div class="demo-play">▶</div>
                        <div class="demo-subs">
                            <div class="demo-sub ko">안녕하세요, 오늘도 좋은 하루 되세요</div>
                            <div class="demo-sub ja">こんにちは、今日も良い一日を</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section" id="languages">
            <div class="section-header">
                <h2 class="section-title"><span class="gradient">Choose Any Language</span></h2>
                <p class="section-desc">Mix and match any two languages for your learning journey</p>
            </div>
            
            <div class="langs-showcase">
                <div class="lang-card en">English</div>
                <div class="lang-card ja">日本語</div>
                <div class="lang-card ko">한국어</div>
                <div class="lang-card zh">中文</div>
            </div>
        </section>
        
        <section class="section" id="features">
            <div class="section-header">
                <h2 class="section-title"><span class="gradient">Powerful Features</span></h2>
                <p class="section-desc">Everything you need for immersive language learning</p>
            </div>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🌐</div>
                    <h3>Multi-language UI</h3>
                    <p>Switch the interface between English, Japanese, Korean, and Chinese instantly</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <h3>Flexible Languages</h3>
                    <p>Choose any two languages for dual subtitles - perfect for any learning combination</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Real-time Sync</h3>
                    <p>Subtitles appear instantly, perfectly synchronized with the audio</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎨</div>
                    <h3>Custom Styling</h3>
                    <p>Personalize colors, fonts, and positioning to match your preferences</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📁</div>
                    <h3>External Subs</h3>
                    <p>Import your own .srt or .vtt subtitle files for any video</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎬</div>
                    <h3>Multi-platform</h3>
                    <p>Works seamlessly on YouTube, Netflix, and more streaming sites</p>
                </div>
            </div>
        </section>
        
        <section class="section" id="install">
            <div class="section-header">
                <h2 class="section-title"><span class="gradient">Get Started in Seconds</span></h2>
                <p class="section-desc">Simple installation, no technical skills required</p>
            </div>
            
            <div class="steps-container">
                <div class="step-card">
                    <div class="step-num">1</div>
                    <h3>Download</h3>
                    <p>Click the button and download the extension ZIP file</p>
                </div>
                <div class="step-card">
                    <div class="step-num">2</div>
                    <h3>Unzip</h3>
                    <p>Extract the downloaded file to a folder on your computer</p>
                </div>
                <div class="step-card">
                    <div class="step-num">3</div>
                    <h3>Load</h3>
                    <p>Go to chrome://extensions, enable Developer mode, and load the folder</p>
                </div>
                <div class="step-card">
                    <div class="step-num">4</div>
                    <h3>Enjoy</h3>
                    <p>Visit YouTube or Netflix and start your language learning journey!</p>
                </div>
            </div>
        </section>
        
        <section class="final-cta">
            <h2>Ready to Level Up Your Learning?</h2>
            <p>Join thousands of language learners using Dual Subs</p>
            <a href="/download" class="btn btn-primary">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
                Download Free Extension
            </a>
        </section>
        
        <footer>
            <p>Made with ❤️ for language learners everywhere</p>
        </footer>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/download')
def download():
    ext_dir = 'my-youtube-dual-subtitle copy 3'
    zip_path = '/tmp/dual-subtitles-extension.zip'
    
    if os.path.exists(zip_path):
        os.remove(zip_path)
    
    shutil.make_archive('/tmp/dual-subtitles-extension', 'zip', ext_dir)
    
    return send_file(
        zip_path,
        mimetype='application/zip',
        as_attachment=True,
        download_name='dual-subtitles-extension.zip'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
