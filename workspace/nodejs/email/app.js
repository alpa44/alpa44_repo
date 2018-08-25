const nodemailer = require('nodemailer');
const fs = require('fs');

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'alpa44@gmail.com',
        pass: 'Tkd3Ghkd5'
    }
});

const mailOptions = {
    from: 'alpa44@gmail.com',
    to: 'alpa44@gmail.com',
    subject: '[jc-coinbot] opportunity files',
    html: '<p>opportunity files</p>',
    attachments: [
        {
            filename: '20180814_opportunity_0.5.csv',
            content: fs.createReadStream('/Users/alpa44/workspace/projects/jc-coinbot/data/20180814_opportunity_0.5.csv')
        },
        {
            filename: '20180814_opportunity_0.2.csv',
            content: fs.createReadStream('/Users/alpa44/workspace/projects/jc-coinbot/data/20180814_opportunity_0.2.csv')
        }
    ]
};

transporter.sendMail(mailOptions, (err, info) => {
    if (err) console.log(err);
    else console.log(info);
});

