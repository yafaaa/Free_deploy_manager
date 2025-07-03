from platforms.models import ProgrammingLanguage, DatabaseType, Feature, Platform

def get_or_create(model, name, **kwargs):
    obj, _ = model.objects.get_or_create(name=name, defaults=kwargs)
    return obj

def add_platform(
    name, description, url, free_tier_description, supports_custom_domains, has_auto_sleep, notes,
    languages, databases, features
):
    platform, _ = Platform.objects.get_or_create(
        name=name,
        defaults={
            'description': description,
            'url': url,
            'free_tier_description': free_tier_description,
            'supports_custom_domains': supports_custom_domains,
            'has_auto_sleep': has_auto_sleep,
            'notes': notes or ''
        }
    )
    for lang in languages:
        platform.supported_languages.add(get_or_create(ProgrammingLanguage, lang))
    for db in databases:
        platform.supported_databases.add(get_or_create(DatabaseType, db))
    for feat in features:
        platform.supported_features.add(get_or_create(Feature, feat))
    platform.save()
    print(f"Added/updated platform: {name}")

# --- Unique lists for all platforms ---
PLATFORMS = [
    {
        'name': 'Render',
        'description': 'Full-stack web services, static sites, small Postgres/Redis databases.',
        'url': 'https://render.com/',
        'free_tier_description': 'Free web services spin down after 15 minutes of inactivity, 750 compute hours/month. Free Postgres DBs expire after 30 days.',
        'supports_custom_domains': True,
        'has_auto_sleep': True,
        'notes': 'Free Postgres DBs deleted after 30 days unless upgraded. Free Redis is ephemeral.',
        'languages': ['Node.js', 'Bun', 'Python', 'Ruby', 'Go', 'Rust', 'Elixir', 'Docker'],
        'databases': ['PostgreSQL', 'Redis'],
        'features': ['Continuous Deployment', 'Automatic HTTPS/SSL', 'Environment Variables', 'Private Networking', 'Web Services', 'Static Sites', 'Background Workers', 'Cron Jobs'],
    },
    {
        'name': 'Railway',
        'description': 'Flexible deployments, many language/DB combos, small apps and APIs.',
        'url': 'https://railway.app/',
        'free_tier_description': 'One-time $5 usage credit, then $5/month free usage. Services stop if limit is hit.',
        'supports_custom_domains': True,
        'has_auto_sleep': False,
        'notes': 'Requires credit card for sustained usage. Trial DBs deleted after 30 days if not upgraded.',
        'languages': ['Bun', 'Clojure', 'Cobol', 'Crystal', 'C#', '.NET', 'Dart', 'Deno', 'Elixir', 'F#', 'Gleam', 'Go', 'Haskell', 'Java', 'Lunatic', 'Node.js', 'PHP', 'Python', 'Ruby', 'Rust', 'Scheme', 'Staticfile', 'Swift', 'Scala', 'Zig', 'Nixpacks'],
        'databases': ['PostgreSQL', 'MySQL', 'MongoDB', 'Redis'],
        'features': ['Automatic Builds', 'Environment Variables', 'Monorepo Support', 'CLI Tool', 'Managed Databases', 'Private Networking', 'Persistent Volumes', 'Cron Jobs'],
    },
    {
        'name': 'Fly.io',
        'description': 'Edge deployments, Dockerized applications, small apps with a global presence.',
        'url': 'https://fly.io/',
        'free_tier_description': 'Usage-based, waives charges for usage under ~$5/month. Limited VM memory, storage, bandwidth.',
        'supports_custom_domains': True,
        'has_auto_sleep': False,
        'notes': 'Requires credit card. Managed Postgres is paid. Persistent storage is billed.',
        'languages': ['Docker', 'Elixir', 'Rails', 'Laravel', 'Django', 'Node.js', 'Rust', 'Python', 'Go', 'Ruby', 'Crystal', '.NET'],
        'databases': ['PostgreSQL', 'SQLite', 'Redis', 'Object Storage', 'MySQL', 'MariaDB'],
        'features': ['Global Distribution', 'Docker Deployment', 'Persistent Volumes', 'Private Networking', 'Custom Domains', 'CLI Workflow'],
    },
    {
        'name': 'Vercel',
        'description': 'Primarily static sites, JAMstack, serverless functions, frontend deployment.',
        'url': 'https://vercel.com/',
        'free_tier_description': 'Hobby plan: 1,000,000 serverless invocations/month, 100 GB bandwidth, 6,000 build minutes.',
        'supports_custom_domains': True,
        'has_auto_sleep': False,
        'notes': 'Hard caps: service pauses if limits exceeded. Best for frontend-heavy apps.',
        'languages': ['JavaScript', 'TypeScript', 'Node.js', 'Go', 'Python', 'Ruby'],
        'databases': ['Supabase', 'Neon', 'PlanetScale', 'Firebase', 'MongoDB'],
        'features': ['Global CDN', 'Automatic SSL', 'Serverless Functions', 'Continuous Deployment', 'Preview Deployments', 'Custom Domains', 'Environment Variables', 'Edge Functions'],
    },
    {
        'name': 'Netlify',
        'description': 'Static sites, JAMstack, serverless functions.',
        'url': 'https://www.netlify.com/',
        'free_tier_description': 'Starter plan: 100 GB bandwidth/month, 300 build minutes/month, 125K serverless invocations/month.',
        'supports_custom_domains': True,
        'has_auto_sleep': False,
        'notes': 'Hard caps: exceeding limits can suspend features or site.',
        'languages': ['JavaScript', 'TypeScript', 'Node.js'],
        'databases': ['Supabase', 'FaunaDB', 'Firebase'],
        'features': ['Global CDN', 'Automatic SSL', 'Netlify Functions', 'Continuous Deployment', 'Preview Deployments', 'Custom Domains', 'Forms', 'Environment Variables'],
    },
    {
        'name': 'Supabase',
        'description': 'PostgreSQL database, authentication, storage, real-time subscriptions, API auto-generation.',
        'url': 'https://supabase.com/',
        'free_tier_description': '500 MB Postgres, 1 GB storage, 2 GB bandwidth/month, 50,000 MAU for Auth.',
        'supports_custom_domains': False,
        'has_auto_sleep': True,
        'notes': 'Projects pause after 1 week of inactivity.',
        'languages': ['JavaScript', 'TypeScript', 'Python', 'C#', 'Swift', 'Kotlin', 'Go', 'Dart', 'PHP', 'Ruby'],
        'databases': ['PostgreSQL'],
        'features': ['Managed PostgreSQL', 'Authentication', 'Real-time Subscriptions', 'Auto-generated APIs', 'Storage', 'Edge Functions'],
    },
    {
        'name': 'Firebase',
        'description': 'Mobile/web app backends, real-time data, authentication, hosting, serverless functions.',
        'url': 'https://firebase.google.com/',
        'free_tier_description': 'Spark Plan: 1 GB Firestore/Realtime DB, 10 GB hosting, 125K Cloud Functions invocations/month.',
        'supports_custom_domains': True,
        'has_auto_sleep': False,
        'notes': 'Part of Google Cloud free tier. Great for mobile/web frontends.',
        'languages': ['JavaScript', 'Java', 'Kotlin', 'Swift', 'Objective-C', 'Unity', 'C++', 'Flutter', 'Node.js', 'Python', 'Go', 'PHP', 'Ruby', 'C#'],
        'databases': ['Firestore', 'Realtime Database'],
        'features': ['Authentication', 'Hosting', 'Cloud Functions', 'Cloud Storage', 'Machine Learning', 'Analytics'],
    },
    {
        'name': 'Deta.sh',
        'description': 'Python/Node.js Micros, simple NoSQL database, file storage.',
        'url': 'https://www.deta.sh/',
        'free_tier_description': 'Forever free, unlimited requests, 10 GB per Deta Base/Drive.',
        'supports_custom_domains': True,
        'has_auto_sleep': True,
        'notes': 'Simple, developer-friendly. Limited to US-East region.',
        'languages': ['Python', 'Node.js'],
        'databases': ['Deta Base'],
        'features': ['Deta Micros', 'Deta Base', 'Deta Drive', 'Custom Domains'],
    },
    {
        'name': 'Glitch',
        'description': 'Quick prototypes, learning, collaborative coding.',
        'url': 'https://glitch.com/',
        'free_tier_description': 'Projects sleep after 5 mins inactivity. 200 MB disk space.',
        'supports_custom_domains': False,
        'has_auto_sleep': True,
        'notes': 'Great for learning, prototyping. Not for production.',
        'languages': ['Node.js', 'Python', 'Ruby', 'Go', 'PHP', 'Static'],
        'databases': ['SQLite', 'External'],
        'features': ['In-browser Editor', 'Collaborative Coding', 'Automatic Deployments', 'Persistent Storage', 'Environment Variables'],
    },
    {
        'name': 'Koyeb',
        'description': 'Global deployments, serverless containers.',
        'url': 'https://www.koyeb.com/',
        'free_tier_description': '750 free instance hours/month, 100 GB egress, 1,000 build minutes.',
        'supports_custom_domains': True,
        'has_auto_sleep': True,
        'notes': 'Good for stateless APIs and microservices.',
        'languages': ['Docker', 'Go', 'Node.js', 'Python', 'Ruby', 'PHP'],
        'databases': ['External'],
        'features': ['Serverless Containers', 'Global Edge Network', 'Automatic Scaling', 'DDoS Protection', 'Custom Domains', 'Private Networking', 'Environment Variables', 'CI/CD'],
    },
    {
        'name': 'Aiven',
        'description': 'Managed free-tier databases (PostgreSQL, MySQL, Redis, Kafka, etc).',
        'url': 'https://aiven.io/',
        'free_tier_description': 'Free tiers for various DBs (e.g., 10GB Postgres). Limits vary.',
        'supports_custom_domains': False,
        'has_auto_sleep': False,
        'notes': 'Requires separate app hosting. Free tiers limited in storage/connections.',
        'languages': ['Any'],
        'databases': ['PostgreSQL', 'MySQL', 'Redis', 'Kafka', 'Cassandra', 'M3DB', 'OpenSearch', 'InfluxDB', 'Grafana'],
        'features': ['Managed Database Hosting', 'SSL Encryption'],
    },
    {
        'name': 'Neon',
        'description': 'Serverless PostgreSQL, branching, compute/storage separation.',
        'url': 'https://neon.tech/',
        'free_tier_description': '3 GB always-free storage, 100 hours/month compute, 10 GB/month transfer.',
        'supports_custom_domains': False,
        'has_auto_sleep': True,
        'notes': 'Excellent for dev/small projects. Cold starts after inactivity.',
        'languages': ['Any'],
        'databases': ['PostgreSQL'],
        'features': ['Serverless PostgreSQL', 'Branching', 'Auto-scaling', 'CLI/API'],
    },
    {
        'name': 'ElephantSQL',
        'description': 'Small, managed PostgreSQL database.',
        'url': 'https://www.elephantsql.com/',
        'free_tier_description': 'Tiny Turtle: 20 MB storage, 5 connections, 20,000 req/month.',
        'supports_custom_domains': False,
        'has_auto_sleep': False,
        'notes': 'Only for basic projects or PoC. No backups on free tier.',
        'languages': ['Any'],
        'databases': ['PostgreSQL'],
        'features': ['Managed PostgreSQL', 'Shared Instance'],
    },
    {
        'name': 'MongoDB Atlas',
        'description': 'Managed NoSQL (MongoDB) database.',
        'url': 'https://www.mongodb.com/cloud/atlas',
        'free_tier_description': 'M0 Cluster: 512 MB-1 GB storage, shared RAM/CPU.',
        'supports_custom_domains': False,
        'has_auto_sleep': True,
        'notes': 'Good for learning/small projects. No backups on free tier.',
        'languages': ['Any'],
        'databases': ['MongoDB'],
        'features': ['Managed MongoDB', 'Cloud Backups', 'Performance Monitoring', 'Security Features', 'Atlas Search', 'Device Sync'],
    },
]

# --- Create all platforms and their links ---
for p in PLATFORMS:
    add_platform(
        name=p['name'],
        description=p['description'],
        url=p['url'],
        free_tier_description=p['free_tier_description'],
        supports_custom_domains=p['supports_custom_domains'],
        has_auto_sleep=p['has_auto_sleep'],
        notes=p['notes'],
        languages=p['languages'],
        databases=p['databases'],
        features=p['features'],
    )

print('All real platforms, languages, databases, and features loaded!')
