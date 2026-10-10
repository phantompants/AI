# Publishing Options

How to get the finished site onto the internet, and how to keep it up to date.

## Contents

1. Choose a path
2. Hosting for plain HTML and CSS
3. Domain names
4. Contact and forms
5. Checking the live site
6. Keeping it current

## 1. Choose a path

| Path | Good for | Trade-off |
|---|---|---|
| Plain HTML and CSS | Portable files, free or cheap hosting | The team updates files, or asks Claude to |
| Website builder | Editing in a browser | Ongoing cost, less portable |

Compare ongoing costs and update effort before choosing.

## 2. Hosting for plain HTML and CSS

| Option | Notes |
|---|---|
| Static hosting service | Many offer free tiers for small sites. Check current limits and terms. |
| GitHub Pages | Free static hosting from an eligible repository. Review current limits. A public repository exposes everything in it, so keep private notes and original photos out. |
| An ordinary web host | Upload the files with the host's file manager or an FTP tool. |

Helpful free tools: Visual Studio Code (edit and preview the files), GitHub Desktop (track and upload changes), and Squoosh (compress images).

## 3. Domain names

A domain name is usually a separate yearly cost, even when hosting is free. A short, easy-to-say name works best (for example the team name plus the year). Point the domain at the host by following the host's own steps.

## 4. Contact and forms

Static hosting cannot run a server-side contact form, and a form collects personal details the team then has to look after. Offer the simplest option that works, in this order:

| Option | Effort | Notes |
|---|---|---|
| Email and phone shown as text | None | Public address gets some spam. Use a forwarding address if you can |
| "Email us" button (mailto link with a subject) | None | Opens the visitor's mail app. Fails for people with none set up |
| Message links for active accounts | Low | Messenger, Instagram, TikTok, WhatsApp. List only accounts someone checks regularly |
| Google Form link | Low | A button that opens the form. Replies go to the team's Google account |
| Form service (for example Formspree) | Medium | Looks like part of the site. Free plans have limits. Check the privacy terms |
| Form script on the host | High | Needs server setup and spam protection. Avoid unless the team wants it |

**WhatsApp.** Use a click-to-chat link in the form `https://wa.me/61XXXXXXXXX`, with the number in international format and no spaces, plus, or leading zero. This publishes the number, so use the public phone number the team already shows, or a separate WhatsApp Business number. For group updates, a WhatsApp channel or group invite link is a separate option. Do not publish a personal number the team has not chosen to make public.

**Messenger.** A link in the form `https://m.me/[page name or ID]` opens a chat with the Facebook page. Test it on a phone before publishing.

Always show the address or number as text as well as a link, because phone and email links do not work for every visitor.

## 4a. Uploading to your host

Upload `index.html` and the `images` folder to the site's web space (any host that serves plain HTML) with the host's file manager or an SFTP tool, keeping the folder names. If the old site's files are there, back them up first. Check the new page on `www` and without it. If the page loads fonts from Google Fonts, say so to the team.

## 5. Checking the live site

After it goes live, on a phone and on a computer:

- Click every donation, sponsor and social link
- Check the menu, images and text are readable
- Check the fundraising figure and its date
- Check the page title and the preview when the link is shared
- Ask a friend who has not seen it to try donating, using only the page

If the site sells things or takes sponsorship payments, check the host's terms first.

## 6. Keeping it current

Update after each milestone: a sponsor confirmed, the car finished, the event starting, the final total. Change the dated figure, add to the Updates section, and republish. Back up the source files after each change. After the event, add a thank-you and the final dated total.
