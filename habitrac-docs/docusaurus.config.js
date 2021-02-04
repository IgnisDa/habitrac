module.exports = {
  title: "habitrac Documentation",
  tagline: "The tagline of my site",
  url: "https://IgnisDa.github.io",
  baseUrl: "/habitrac/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",
  organizationName: "IgnisDa",
  projectName: "habitrac",
  themeConfig: {
    navbar: {
      title: "habitrac",
      logo: {
        alt: "habitrac Logo",
        src: "img/logo.svg",
      },
      items: [
        {
          href:
            "https://github.com/IgnisDa/habitrac",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      copyright: `Copyright © ${new Date().getFullYear()} Diptesh Choudhuri, Built with Docusaurus.`,
    },
  },
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          routeBasePath: "/",
          editUrl:
            "https://github.com/IgnisDa/habitrac/edit/main/habitrac-docs/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
};
