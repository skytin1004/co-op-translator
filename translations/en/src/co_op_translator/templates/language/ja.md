---
title: "How to Use Azure App Service Static Site (preview)"
description: "How to use Azure App Service Static Site (preview)"
---

# How to Use Azure App Service Static Site (preview)

Azure App Service Static Site is a web-hosting environment optimized for static web apps such as JavaScript, HTML, and CSS sites. It is designed to provide global scale, serverless API integration, and seamless GitHub integration.

With this feature, you can:

- Quickly deploy static web applications.
- Host your static web apps that automatically scale.
- Connect with serverless APIs.
- Enable one-click deployment directly from GitHub repositories.

You will learn in this document how to start using Azure App Service Static Site from deployment to configuration.

## Prerequisites

Before you begin, ensure you have:

- An active Azure subscription.
- A GitHub account with a repository containing your static site.

## Creating a Static Site

1. Go to the Azure portal.
2. Create a new Static Site resource.
3. Connect your GitHub repository for automatic deployment.
4. Configure build and deployment settings.

## Deployment and Configuration

- After connecting your GitHub repo, commits to the default branch trigger automatic continuous deployment.
- Use environment variables for configuration.
- Monitor build and deployment status in the Azure portal.

For detailed steps, refer to the [Azure App Service Static Site documentation](https://docs.microsoft.com/azure/app-service/static).

## Additional Resources

- [Azure App Service documentation](https://docs.microsoft.com/azure/app-service/)
- [Getting started with GitHub Actions](https://docs.github.com/actions/learn-github-actions/understanding-github-actions)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->