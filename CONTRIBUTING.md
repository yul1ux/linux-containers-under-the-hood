# Contributing

ဤ project သည် Linux container internals ကို မြန်မာဘာသာဖြင့် နည်းပညာတိကျစွာ ရှင်းပြရန် ရည်ရွယ်သည်။ Contribution များသည် approved architecture၊ Phase 3 research requirements နှင့် Phase 4 editorial standards ကို ထိန်းသိမ်းရမည်။

## Contribution အမျိုးအစားများ
- Technical correction: kernel behavior၊ system call/API၊ OCI specification၊ runtime implementation၊ security နှင့် version-specific claims။
- Burmese editorial correction: grammar၊ readability၊ terminology နှင့် natural wording။ Technical meaning မပြောင်းရ။
- Documentation defect: navigation၊ links၊ rendering၊ Mermaid၊ accessibility နှင့် mobile layout။
- Lab feedback: သီးခြားခွင့်ပြုထားပြီး အမှန်တကယ် လုပ်ဆောင်ခဲ့သော lab မှ sanitized evidence သာ။

## Evidence
Technical correction တွင် chapter/section၊ လက်ရှိ claim၊ အကြံပြုချက်၊ official/versioned source နှင့် သက်ဆိုင်ရာ release ကို ဖော်ပြပါ။ Standard-defined နှင့် implementation-specific behavior ကို ခွဲပါ။ Lab feedback တွင် OS/kernel/tool versions၊ privilege level၊ exact command၊ actual output၊ expected-vs-actual နှင့် cleanup result ပါရမည်။ မစမ်းသပ်ထားသောအချက်ကို tested ဟု မဖော်ပြရ။

## Editorial standards
မြန်မာ Unicode ကို အဓိကအသုံးပြုပါ။ Command၊ code၊ API၊ file path နှင့် kernel identifier များကို မပြောင်းရ။ Ko Ei Maung ၏ API – လိုတိုရှင်း ကို အထွေထွေ editorial inspiration အဖြစ်သာ သဘောထားပြီး စာသား၊ ထူးခြားသော ဥပမာ သို့မဟုတ် distinctive style ကို မကူးယူရ။

## Scope and safety
Approved architecture သည် 6 Parts / 19 Chapters ဖြစ်သည်။ Chapter files များသည် navigation scaffold သာဖြစ်ပြီး Phase 6 Chapter Production မစတင်သေးပါ။ Phase 7 Lab Validation မစတင်သေးပါ။ DEC-009/010 Deferred ဖြစ်သည်။ Host inventory၊ VM provisioning၊ privileged lab သို့မဟုတ် everyday host ပေါ်တွင် privileged experiment များကို ဤ setup ကြောင့် ခွင့်ပြုသည်ဟု မယူဆရ။ Credentials၊ tokens၊ keys၊ usernames၊ hostnames၊ private IPs၊ home paths၊ serial numbers သို့မဟုတ် personal data မတင်ရ။

## Pull Requests
PR တစ်ခုကို scope တစ်ခုတည်းအပေါ် အာရုံစိုက်ပါ။ Affected section၊ evidence/source၊ validation status နှင့် cleanup status ကို ဖော်ပြပါ။ Strict MkDocs build နှင့် structure check အောင်မြင်ရမည်။ မစမ်းသပ်ထားသည့် lab ကို ရှင်းလင်းစွာဖော်ပြပါ။

## Licensing
Book prose/original diagrams: CC BY 4.0။ Original code examples/lab scripts: MIT။ Third-party content သည် မူလ license နှင့် attribution အတိုင်းဖြစ်သည်။
