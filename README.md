## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

Running on Arch X11 with Nvidia

```bash
# if you are running on Wayland you may encounter an issue, just switch to X11 and then run:
WEBKIT_DISABLE_DMABUF_RENDERER=1 npm run tauri dev
```

## Building

To create a production version:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.
