---
title: "Pag-deploy ng iyong first React app sa Azure Static Web Apps"
description: "Matutunan kung paano mag-deploy ng isang React app gamit ang Azure Static Web Apps mula sa zero."
---

# Pag-deploy ng iyong first React app sa Azure Static Web Apps

Ang Azure Static Web Apps ay isang serbisyo na nagpapadali sa pag-host at pag-deploy ng mga static web application, kabilang ang mga React app. Sa gabay na ito, malalaman mo kung paano gumawa ng React app mula sa simula at i-deploy ito sa Azure Static Web Apps gamit ang GitHub repository.

## Mga kinakailangan

- [Node.js](https://nodejs.org/) naka-install sa iyong makina
- GitHub account
- Azure account
- Visual Studio Code (opsyonal, para sa pag-edit ng code)

## Hakbang 1: Gumawa ng bagong React app

Una, gumawa tayo ng bagong React app gamit ang [Create React App](https://create-react-app.dev/):

```bash
npx create-react-app my-react-app
cd my-react-app
```

Subukan patakbuhin ang app locally:

```bash
npm start
```

Dapat makita mo ang default React homepage sa iyong browser sa `http://localhost:3000`.

## Hakbang 2: I-push ang iyong app sa GitHub

1. Gumawa ng bagong repository sa GitHub.
2. Sa iyong proyekto, i-initialize ang git:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```

Palitan ang `your-username/your-repo` ng iyong sariling GitHub repository URL.

## Hakbang 3: Gumawa ng Azure Static Web App sa portal

1. Pumunta sa [Azure portal](https://portal.azure.com).
2. Mag-click sa **Create a resource** at hanapin ang **Static Web Apps**.
3. Piliin ang **Create**.
4. Punan ang mga kinakailangang information, at sa seksyon ng **Deployment Details**, piliin ang GitHub bilang source na provider.
5. I-authorize ang Azure na ma-access ang iyong GitHub account.
6. Piliin ang repository at branch na gusto mong i-deploy (halimbawa, `main`).
7. Sa **Build Details**, itakda ang Framework preset sa **React**.
8. I-click ang **Review + create** at pagkatapos ay **Create**.

## Hakbang 4: I-monitor ang deployment

Pagkatapos simulan ang deployment, awtomatikong gagawa si Azure ng GitHub Actions workflow para i-build at i-deploy ang iyong app. Maaari mong makita ang status ng workflow sa iyong GitHub repository sa ilalim ng **Actions** tab.

Kapag tapos na, bibigyan ka ng URL papunta sa live na website.

## Pagsusuri

Buksan ang ibinigay na URL sa browser mo at dapat makita mo ang iyong running React app sa Azure Static Web Apps!

## Karagdagang impormasyon

Para sa mas detalyadong gabay at advanced na features ng Azure Static Web Apps, bisitahin ang opisyal na dokumentasyon:

- [Azure Static Web Apps documentation](https://learn.microsoft.com/azure/static-web-apps/)
- [Create React App documentation](https://create-react-app.dev/docs/getting-started/)

[!TIP]
Para sa mas madaling pag-deploy, maaari kang gumamit ng [GitHub App](https://github.com/apps/azure-static-web-apps) para sa Azure Static Web Apps.

Happy coding!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinakapinagkakatiwalaang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->