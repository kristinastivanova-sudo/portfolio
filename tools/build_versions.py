#!/usr/bin/env python3
"""Build the portfolio versions from src/.

src/ holds the source pages (the startup version). It is not deployed (.vercelignore).
The site root shows a blank page; each version lives in a folder with a random code,
so nobody can find one version from another. Run after any change in src/:
    python3 tools/build_versions.py
"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
PAGES = ['index', 'homefans', 'grow-by-mia', 'katalysta', 'vitesse-running', 'geegee', 'ahoy-connect',
         'luxe-lips', 'plantsnap', 'story-of-lola', 'learnify', 'drops-of-emotions', 'mymultisport']

# Wording used on several pages (titles also appear in homepage cards and next-project cards).
ENT_ALL = [
    ('Scaling an AI-driven EdTech platform in a new market', 'Launching an AI-driven EdTech platform in a new market'),
    ('Planning and building social content for a B2B community platform', 'Building a scalable B2B content engine for a SaaS platform'),
    ('A last-minute Black Friday campaign on a small budget', 'Doubling Black Friday sales with a staged paid-social campaign'),
    ('Leading marketing for a football travel marketplace, with AI built into the workflow',
     'Leading growth marketing for a football travel marketplace, with AI-enabled workflows'),
]

ENT_PAGE = {
 'index': [
  ("Homefans · current role", "Homefans · Consulting engagement"),
  ("AI-first growth marketing", "Full-funnel growth, scaled with AI"),
  ("with a designer's touch", "and a customer-experience lens"),
  ("I'm Kristina, a growth marketing manager with 10+ years in startups and hands-on UX training. I lead teams, run paid, email and funnels, and use AI to design, build and ship faster.",
   "I'm Kristina, a growth marketing manager with 10+ years across EdTech, mobile apps, SaaS and marketplaces. I lead cross-functional teams, own paid media, lifecycle and conversion, and build AI-enabled workflows that make marketing faster and more measurable."),
  ("Growth work, measured in revenue and retention", "Measurable impact across acquisition, conversion and retention"),
  ("Running the social and PPC teams, owning Meta Ads and email, and connecting Claude to the marketing stack.",
   "As a consultant, leading the social and PPC teams and setting up their processes, owning Meta Ads and lifecycle email, and aligning campaigns with sales and supply."),
  ("Lead magnets, email flows and paid ads that turned cold leads into buyers of a €5,000 flagship program.",
   "A full-funnel system of lead magnets, lifecycle email and paid media that converted cold audiences into buyers of a €5,000 program."),
  ("Fear-specific lead magnets, concrete career messaging and behavior-based emails that turned a 0.7% conversion launch in Georgia into a profitable engine.",
   "Market entry in Georgia: audience research, outcome-focused messaging and behaviour-based lifecycle email that lifted conversion from 0.7% to 1.8% and made the market profitable."),
  ("Performance marketing across Google UAC, Apple Search Ads and Meta, optimized for real runs instead of installs.",
   "Performance marketing across Google UAC, Apple Search Ads and Meta, measured on activation (real runs), not installs."),
  ("Research and positioning, then paid acquisition across TikTok, Snapchat and Meta in New Zealand, Australia and the UK.",
   "Research-led positioning, then multi-channel paid acquisition across three markets, with cost per install down 77%."),
  ("Six content pillars, a weekly calendar across LinkedIn, Twitter and Facebook, and LinkedIn ads with retargeting.",
   "A repeatable content system with six pillars, a cross-channel calendar and LinkedIn retargeting for a B2B data-intelligence platform."),
  ("Shorter paid-media engagements for e-commerce and app brands.", "Focused paid-media engagements for e-commerce and app brands."),
  ("Claude, connected to the marketing stack", "AI-enabled marketing operations"),
  ("Instead of exporting data and switching between tabs, I connect Claude directly to the tools I use. It does the legwork, and I make the calls.",
   "I connect Claude directly to the ad platforms, analytics, CRM and design tools, so reporting, segmentation and creative production are faster and more consistent, while every decision stays with a person."),
  ("The full funnel, not just one channel", "End-to-end ownership of the growth funnel"),
  ("Automations, nurture flows and copy that move subscribers from first signup to repeat purchase.",
   "Automated journeys, segmentation and consent-aware email programs that move customers from first signup to repeat purchase."),
  ("Meta Ads for cold and warm audiences, with creative testing and budgets tied to cost per lead and ROAS.",
   "Meta and Google campaigns with structured creative testing and budgets managed against CAC, CPA and ROAS."),
  ("Landing pages, webinars and lead magnets, plus the UX fixes that lift conversion on the product side.",
   "Landing pages, webinars and lead magnets, plus UX improvements that lift conversion across the customer journey."),
  ("User research, personas and messaging that give content and social a clear, consistent voice.",
   "Customer research, personas and messaging frameworks that keep every channel consistent."),
  ("UX case studies that sharpen how I spot and fix conversion problems inside the product.",
   "UX case studies showing how I use research and design to diagnose and fix conversion problems inside the product."),
  ("Looking for someone to own growth across email, paid and funnels? I'd like to hear about it.",
   "Looking for someone to own growth across paid media, lifecycle and conversion, and to bring AI into how your team works? I'd like to hear about it."),
 ],
 'homefans': [
  ("Team lead &amp; hands-on growth", "Team leadership · consulting"),
  ("Homefans · Marketing Lead · Football travel marketplace", "Homefans · Growth Lead (consultant) · Football travel marketplace"),
  ("Marketing Lead: team of 4, plus hands-on", "Growth lead (consultant): team of 4, plus hands-on"),
  ("At Homefans I run two teams, social media and PPC, and own Meta Ads and email myself. I work closely with host onboarding on supply and with sales on joint campaigns. Claude is connected to most of the stack, so a small team covers a lot of ground.",
   "As a consultant, I took the lead of the social media and PPC teams at Homefans and set up the processes they run on: planning, prioritisation and reporting. I also own Meta Ads and lifecycle email, working across host onboarding, sales and engineering. With Claude connected to most of the stack, a small team covers a lot of ground."),
 ],
 'grow-by-mia': [
  ("a full funnel of lead magnets, webinars, email flows and Meta Ads that sold a €5,000 flagship program to 100+ women.",
   "a full-funnel system of lead magnets, webinars, lifecycle email and Meta Ads that sold a €5,000 flagship program to 100+ customers."),
 ],
 'katalysta': [
  ("How fear-specific lead magnets, concrete career messaging and behavior-based emails turned a 0.7% conversion launch in Georgia into a profitable, scalable engine within 12 months.",
   "Market entry in Georgia: targeted lead magnets, outcome-focused career messaging and behaviour-based email turned a 0.7% conversion launch into a profitable, scalable market within 12 months."),
 ],
 'geegee': [
  ("Research, positioning and paid acquisition for a Gen Z MicroSports app. After defining who it was for and what to say, I ran install campaigns across five channels over five months, cutting the cost of an install by 77% along the way.",
   "Research-led positioning and multi-channel paid acquisition for a Gen Z sports app: five channels, three markets and a 77% lower cost per install in five months."),
 ],
 'ahoy-connect': [
  ("A content system for AhoyConnect, a data intelligence platform for community managers: six content pillars, a weekly cross-channel calendar, and LinkedIn ads that tested what got community builders to click.",
   "A repeatable content system for AhoyConnect, a data-intelligence SaaS platform for community managers: six content pillars, a weekly cross-channel calendar and LinkedIn campaigns that tested what drove engagement."),
 ],
 'story-of-lola': [
  ("Build an audience, warm it up, then sell: a three-stage Black Friday campaign for a small fashion brand, plus a homepage fix that took store conversion from 0.1% to 1.13%.",
   "A three-stage campaign (build the audience, warm it up, convert) for a fashion e-commerce brand, plus a homepage fix that lifted store conversion from 0.1% to 1.13%."),
 ],
}


VERSIONS = {
    '': ('main site (startup)', [], {}),          # the public root: indexable
    '48217': ('startup, hidden copy', [], {}),
    '90563': ('enterprise', ENT_ALL, ENT_PAGE),
}

def paths(t, code):
    base = '/' + code + '/' if code else '/'
    t = re.sub(r'(href|src)="(?:\./)?(assets|prototypes)/', r'\1="/\2/', t)
    t = re.sub(r'url\((["\']?)(?:\./)?assets/', r'url(\1/assets/', t)
    t = t.replace('href="favicon.svg"', 'href="/favicon.svg"')
    t = re.sub(r'href="(?:\./)?([a-z0-9-]+\.html)(#[^"]*)?"', lambda m: f'href="{base}{"" if m.group(1)=="index.html" else m.group(1)}{m.group(2) or ""}"', t)
    t = re.sub(r'href="\./(#[^"]*)?"', lambda m: f'href="{base}{m.group(1) or ""}"', t)
    return t

def main():
    bad = []
    for code, (name, allmap, pagemap) in VERSIONS.items():
        out = os.path.join(ROOT, code) if code else ROOT; os.makedirs(out, exist_ok=True)
        for p in PAGES:
            t = open(os.path.join(SRC, p + '.html'), encoding='utf-8').read()
            for a, b in allmap:
                t = t.replace(a, b)
            for a, b in pagemap.get(p, []):
                if a not in t: bad.append(f'{name}/{p}: {a[:70]}')
                t = t.replace(a, b)
            t = paths(t, code)
            if code:
                t = t.replace('<meta name="viewport"', '<meta name="robots" content="noindex, nofollow">\n<meta name="viewport"', 1)
            open(os.path.join(out, p + '.html'), 'w', encoding='utf-8').write(t)
        print(f'/{code} ({name}) built')
    if bad:
        print('Source text changed, update the map:\n  ' + '\n  '.join(bad)); sys.exit(1)

if __name__ == '__main__':
    main()
