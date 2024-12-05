# Let's encrypt manual certs with cerbot

This assumes you're using nginx. If you're using a different server software (e.g.: apache), just change the parts that use nginx to what you're using.

Note: The official website provides very useful/comprehensive instructions [certbot](https://certbot.eff.org/instructions).

## Install certbot

`apt-get certbot`, `pacman -Syu certbot`, etc...\\
You might also want to install your server software plugin (if available), e.g.: `pacman -Syu certbot-nginx`.

Note: use `sudo nginx -s reload` or `sudo systemctl restart nginx` to reload nginx.

## Run certbot

  * For normal domains, e.g. `example.com`, there's no need to do a manual setup. Run `sudo certbot --nginx` or whatever the site instructs. Stop reading here.
  * For wildcard domain, e.g. `*.example.com`, the automatic process requires dns service support. This isn't available for most, but you should check for new so it can be done automatically. Otherwise, we need a manual setup. Run `certbot certonly --manual --preferred-challenges dns`.

## Follow certbot instruction

  - Enter email address.
  - Read and accept terms.
  - Choose if you want to share email adress with EFF.
  - Enter domain: e.g. `*.example.com, example.com` (probably want both, remeber the mistake?).
  - Go to DNS settings (e.g. vultr dns) and create a new DNS TXT record like so:
    * Name: _acme-challenge
    * Value/Data: as1...5&b (given value)
    * TLS: as low as available.
  - Press continue on certbot.
  - After process finishes, delete created DNS TXT record.

NOTE: The renewal of the TLS certificate will be manual (see next section).

## Manual renew

We can just enter the same command we ran to create the certificate(s). Certbot will
detect the certs are due for renewal and give us the new dns challenge. We can also
create a script to set up the dns/http challenge and use `certbot renew` with the
script.

## Automatic renew

Run `certbot renew` for interactive prompts (only if you didn't have to do a manual setup).

## Delete certs

Run `certbot delete` for interactive prompts.

## Tell nginx to use the certificates

  * `vim /etc/nginx/sites-available/example.com`.
  * Change port 80 to port 443 (for https):

```bash
  listen 443 default_server;
  listen [::]:443 default_server;
```

  * Add to the file:

```bash
server {
  ... # previous stuff that' already there

  ssl on;
  ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
}
```bash

  * Test config with: `sudo nginx -t`.
  * Restart nginx with: `sudo systemctl restart nginx`.

NOTE: might also want to unblock https in firewall config, e.g. `ufw allow 'Nginx HTTPS`' or run `sudo ufw app list` to find possible entries.

## Redirect http to https

  * `vim /etc/nginx/sites-available/example.com` (yes the same file).
  * add new server block:

```bash
server {
  # redirect all http to https
  server_name example.com www.example.com;
  return 301 https://example.com$request_uri;
}
```

This listens to port 80 (https) and redirects to port 443 (https).

## Performance stuff

Don't forget to test config (`sudo nginx -t`) and restart nginx (`sudo systemctl restart nginx`) after any of this changes.

### Enable HTTP/2

Enables parallel file requesting. Should change server block to:

```bash
server {
   listen 443 http2 default_server;
   listen [::]:443 http2 default_server;

   ... # all other content
}
```

### Enable gzip compression

Decrease file size during transmission. **WARNING** there can be security vulnerabilities with gzip compression.\\
Should add to server block:

```bash
server {
   ... # previous content

   gzip on;
   gzip_types application/javascript image/* text/css;
   gunzip on;
}
```

This will ensure that javascript files, images, and CSS files are always compressed.

### Enable client-side caching

Some files don’t ever change, or rarely change, so there’s no need to have users
re-download the latest version. You can set cache control headers to provide hints
to browsers to let them know what files they shouldn’t request again.

```bash
server {
   ... # after the location / block

   location ~* \.(jpg|jpeg|png|gif|ico)$ {
       expires 30d;
    }
    location ~* \.(css|js)$ {
       expires 7d;
    }
}
```

### Dynamically route subdomains to folders

If you have subdomains, chances are you don’t want to have to route every
subdomain to the right folder. It’s a maintenance pain. Instead, create a wildcard
server block for it, routing to the folder that matches the name:

```bash
server {
       server_name ~^(www\.)(?<subdomain>.+).jgefroh.com$ ;
       root /var/www/jgefroh.com/$subdomain;
}
server {
        server_name ~^(?<subdomain>.+).jgefroh.com$ ;
        root /var/www/jgefroh.com/$subdomain;
}
```
