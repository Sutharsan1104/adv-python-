import qrcode
data = "https://gemini.google.com/app/b55b8fe21859b771?is_sa=1&is_sa=1&android-min-version=301356232&ios-min-version=322.0&campaign_id=bkws&utm_source=sem&utm_source=google&utm_medium=paid-media&utm_medium=cpc&utm_campaign=bkws&utm_campaign=2024enIN_gemfeb&pt=9008&mt=8&ct=p-growth-sem-bkws&gclsrc=aw.ds&gad_source=1&gad_campaignid=20357620749&gbraid=0AAAAApk5BhlysR3GqmgwnYXAtq_kWlU2y&gclid=CjwKCAjwxrLHBhA2EiwAu9EdM1SGH0_BMLu7XX1tOQlkZ7buYPczOSTVSQAZvuiS-iNI8Cy20dOrJxoCfyUQAvD_BwE"
qr = qrcode.make(data)
qr.save("google_qr.png")
print("QR Code Has Been Generated")