import repositoryConfig from "./eslint.config.mjs";

export default [
  ...repositoryConfig,
  {
    name: "wavelum/import-order-enforcement",
    rules: {
      "import/order": "error",
    },
  },
];
