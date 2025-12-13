import { Resource } from '../types';

export const resources: Resource[] = [
  {
    id: '1',
    title: 'OWASP ZAP',
    description: 'Open-source web application security scanner. Perfect for finding vulnerabilities in web applications during development and testing.',
    url: 'https://www.zaproxy.org/',
    type: 'tool',
    category: 'Testing',
    tags: ['scanning', 'penetration-testing', 'open-source'],
    featured: true,
    author: 'OWASP'
  },
  {
    id: '2',
    title: 'Burp Suite Community',
    description: 'Industry-standard toolkit for web security testing. Essential for manual security assessment and vulnerability discovery.',
    url: 'https://portswigger.net/burp/communitydownload',
    type: 'tool',
    category: 'Testing',
    tags: ['proxy', 'scanning', 'penetration-testing'],
    featured: true,
    author: 'PortSwigger'
  },
  {
    id: '3',
    title: 'JWT.io Debugger',
    description: 'Online tool to decode, verify and generate JSON Web Tokens. Essential for understanding and debugging JWT implementations.',
    url: 'https://jwt.io/',
    type: 'tool',
    category: 'Authentication',
    tags: ['jwt', 'debugging', 'tokens'],
    featured: false,
    author: 'Auth0'
  },
  {
    id: '4',
    title: 'Web Security Academy',
    description: 'Free online training from PortSwigger covering all aspects of web security including SQL injection, XSS, and CSRF.',
    url: 'https://portswigger.net/web-security',
    type: 'video',
    category: 'Learning',
    tags: ['education', 'tutorials', 'hands-on'],
    featured: true,
    author: 'PortSwigger'
  },
  {
    id: '5',
    title: 'LiveOverflow',
    description: 'YouTube channel with in-depth security tutorials, CTF walkthroughs, and hacking explanations.',
    url: 'https://www.youtube.com/c/LiveOverflow',
    type: 'video',
    category: 'Learning',
    tags: ['youtube', 'ctf', 'tutorials'],
    featured: true,
    author: 'LiveOverflow'
  },
  {
    id: '6',
    title: 'OWASP Top 10',
    description: 'Standard awareness document for developers about the most critical security risks to web applications.',
    url: 'https://owasp.org/www-project-top-ten/',
    type: 'paper',
    category: 'Standards',
    tags: ['owasp', 'best-practices', 'guidelines'],
    featured: true,
    author: 'OWASP'
  },
  {
    id: '7',
    title: 'CSP Cheat Sheet',
    description: 'Comprehensive guide to Content Security Policy headers and how to implement them effectively.',
    url: 'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html',
    type: 'paper',
    category: 'Standards',
    tags: ['csp', 'headers', 'defense'],
    featured: false,
    author: 'OWASP'
  },
  {
    id: '8',
    title: 'Cryptopals Challenges',
    description: 'A collection of cryptography challenges that teach real-world cryptography concepts through practice.',
    url: 'https://cryptopals.com/',
    type: 'paper',
    category: 'Cryptography',
    tags: ['crypto', 'challenges', 'learning'],
    featured: false,
    author: 'Cryptopals'
  },
  {
    id: '9',
    title: 'Nuclei',
    description: 'Fast and customizable vulnerability scanner based on simple YAML-based templates.',
    url: 'https://github.com/projectdiscovery/nuclei',
    type: 'tool',
    category: 'Testing',
    tags: ['scanning', 'automation', 'open-source'],
    featured: false,
    author: 'ProjectDiscovery'
  },
  {
    id: '10',
    title: 'SecurityHeaders.com',
    description: 'Free tool to analyze HTTP response headers and provide security recommendations.',
    url: 'https://securityheaders.com/',
    type: 'tool',
    category: 'Testing',
    tags: ['headers', 'analysis', 'free'],
    featured: false,
    author: 'Scott Helme'
  },
  {
    id: '11',
    title: 'HackTheBox',
    description: 'Online platform with vulnerable machines for practicing penetration testing skills.',
    url: 'https://www.hackthebox.com/',
    type: 'tool',
    category: 'Practice',
    tags: ['ctf', 'practice', 'pentesting'],
    featured: false,
    author: 'HackTheBox'
  },
  {
    id: '12',
    title: 'SANS Reading Room',
    description: 'Extensive library of security whitepapers and research papers on various topics.',
    url: 'https://www.sans.org/white-papers/',
    type: 'paper',
    category: 'Research',
    tags: ['research', 'whitepapers', 'advanced'],
    featured: false,
    author: 'SANS Institute'
  }
];
