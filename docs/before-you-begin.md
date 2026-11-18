# Before You Begin

ဒီစာအုပ်ကို စဖတ်ဖို့ Linux kernel programming ကို ကြိုကျွမ်းကျင်ထားစရာ မလိုပါဘူး။ Terminal မှာ command အနည်းငယ် သုံးဖူးပြီး file၊ directory နဲ့ process ဆိုတာကို အကြမ်းဖျင်း သိထားရင် စလို့ရပါတယ်။ ကျန်တာတွေကို အခန်းလိုက် ရှင်းပြသွားပါမယ်။

## ကြိုသိထားရင် ကောင်းတာတွေ

အောက်ပါအချက်တွေကို သိထားရင် အခန်းတွေကို လိုက်ဖတ်ရတာ ပိုလွယ်ပါလိမ့်မယ်။ အကုန် အဆင့်မြင့်အထိ သိဖို့ မလိုပါဘူး။

- Linux terminal မှာ command ရိုက်ပြီး အခြေခံလုပ်ဆောင်မှုတွေ လုပ်ဖူးခြင်း။
- File နဲ့ directory ဘာကွာသလဲ၊ `/etc/app.conf` လို path တစ်ခုကို ဘယ်လိုဖတ်ရသလဲ သိခြင်း။
- `/etc`၊ `/var`၊ `/proc` လို Linux directory တွေကို အကြမ်းဖျင်း သိခြင်း။
- Process တစ်ခု run နေတယ်ဆိုတာနဲ့ PID (Process ID) ရှိတယ်ဆိုတာ နားလည်ခြင်း။
- User၊ group နဲ့ file permission ရဲ့ အခြေခံကို သိခြင်း။
- `cat`၊ `ls`၊ `ps`၊ `uname` လို command တွေကို တစ်ခါတလေ သုံးဖူးခြင်း။

တချို့ မသိသေးလည်း ပြဿနာမရှိပါဘူး။ အခန်းတစ်ခုထဲမှာ လိုလာတဲ့အခါ အဓိပ္ပာယ်နဲ့ အသုံးပြုပုံကို ရှင်းပြထားပါမယ်။ **C programming ကိုလည်း ကြိုမသိထားရပါဘူး။** အခန်းတချို့မှာ C code နမူနာ တွေ့ရင် ဘာကို ပြချင်တာလဲဆိုတာ ရှင်းပြထားပါတယ်။

**Docker၊ Podman၊ Kubernetes ကိုလည်း ကြိုမလေ့လာထားရပါဘူး။** Tool တစ်ခုချင်းစီရဲ့ command ကို အလွတ်ကျက်တာထက် အဲဒီ tool တွေအောက်မှာ ဘယ် mechanism တွေ အလုပ်လုပ်နေသလဲကို အဓိကထားပါတယ်။ သက်ဆိုင်ရာအခန်းရောက်မှ လိုအပ်တဲ့ tool နဲ့ term တွေကို မိတ်ဆက်ပေးပါမယ်။ Container runtime တစ်ခုကို အရင် install လုပ်ထားစရာလည်း မလိုပါဘူး။ Concept နဲ့ diagram တွေကို ပုံမှန် ဖတ်လို့ရပါတယ်။

## ကိုယ့် environment က ဘာလဲ

ဒီစာအုပ်ကို ဖတ်ဖို့ Linux စက် မလိုပါဘူး။ ဒါပေမဲ့ Lab တွေကို လက်တွေ့လုပ်ချင်ရင် Linux kernel ကို တိုက်ရိုက်သုံးနိုင်တဲ့ environment လိုပါတယ်။

| ကိုယ့်စက် | Concept ဖတ်ဖို့ | Lab လုပ်ဖို့ |
|---|---|---|
| Linux (native) | ရတယ် | Lab ရဲ့ requirement ကို စစ်ပြီး လုပ်နိုင်တယ်။ Distribution နဲ့ kernel version အလိုက် ကွာနိုင်တယ် |
| Windows | ရတယ် | Linux VM (သို့) WSL2 လို Linux environment လိုနိုင်တယ်။ Windows ကိုယ်တိုင်က Linux kernel မဟုတ်ဘူး |
| macOS | ရတယ် | Linux VM လိုတယ်။ macOS ကိုယ်တိုင်က Linux kernel မဟုတ်ဘူး |

> **Docker Desktop၊ WSL2 နဲ့ `podman machine`:** Windows (သို့) macOS မှာ ဒီ tool တွေနဲ့ Linux container run ရင် container တွေက ကိုယ့်စက်ရဲ့ OS kernel ကို မသုံးပါဘူး။ နောက်ကွယ်မှာ Linux VM တစ်ခု run ထားပြီး အဲဒီ VM ရဲ့ Linux kernel ကို သုံးတာပါ။ ဒါကြောင့် ကိုယ့်စက်ရဲ့ OS version နဲ့ container ထဲက kernel version မတူတာကို တွေ့ရရင် ပုံမှန်ပါပဲ။ ဒီစာအုပ်မှာ "host kernel" လို့ပြောရင် container ကို တကယ် run နေတဲ့ Linux kernel ကို ဆိုလိုပါတယ်။

ကိုယ်ရောက်နေတဲ့ terminal က Linux လား စစ်ချင်ရင် `uname -srm` ကို run ကြည့်ပါ (read-only command ပါ)။ Linux terminal မှာ `Linux` လို့ ပေါ်ပြီး macOS terminal မှာတော့ `Darwin` လို့ ပေါ်ပါလိမ့်မယ်။

**Baseline ကို အတည်မပြုရသေးပါဘူး။** ဒီစာအုပ်အတွက် သုံးမယ့် host operating system၊ VM software နဲ့ Fedora guest baseline ကို အခုအချိန်မှာ ဆုံးဖြတ်ထားခြင်း မရှိသေးပါဘူး။ ဒါကြောင့် စာဖတ်သူတိုင်းမှာ တူညီတဲ့ Linux version (သို့) VM တစ်ခု ရှိရမယ်လို့ မဆိုလိုပါဘူး။ Lab တစ်ခုချင်းစီမှာ လိုအပ်တဲ့ environment နဲ့ version ကို သီးခြားဖော်ပြပါမယ်။ အဲဒီလိုအပ်ချက် မပြည့်သေးရင် ကိုယ့်နေ့စဉ်သုံး host ပေါ်မှာ privileged command တွေကို အစားထိုးစမ်းတာမျိုး မလုပ်ပါနဲ့။ Lab မလုပ်နိုင်သေးရင်လည်း အခန်းရဲ့ explanation နဲ့ diagram တွေကို ဆက်ဖတ်နိုင်ပါတယ်။

## Lab မလုပ်ခင် အရင်စစ်ပါ

Lab တွေက အယူအဆတွေကို ပိုနားလည်စေပါတယ်။ ဒါပေမဲ့ Linux host ပေါ်က command တချို့က process စတင်တာ၊ file ပြောင်းတာ၊ permission သုံးတာ (သို့) system configuration ကို ပြင်တာမျိုး လုပ်နိုင်ပါတယ်။ ဒါကြောင့် command တစ်ခုချင်းစီကို မသိဘဲ ကူးထည့်မလုပ်ပါနဲ့။ Lab တစ်ခုကို မစခင် -

1. **Lab status ကို ကြည့်ပါ။** `Designed, not tested` ဆိုရင် ဒီစာအုပ်အတွက် သီးခြား environment မှာ run ပြီး အတည်မပြုရသေးတာပါ။ စမ်းသပ်ပြီးသားလို့ မယူဆပါနဲ့။ အခန်းထဲက expected output တွေက ရလဒ်ကို ဘယ်လိုဖတ်ရမလဲ ပြတာသာ ဖြစ်ပြီး စမ်းသပ်ပြီးသား output မဟုတ်ပါဘူး။
2. **Risk level နဲ့ requirement ကို စစ်ပါ။** Lab တစ်ခုချင်းစီမှာ Risk level (Low၊ Medium၊ High)၊ လိုအပ်တဲ့ distribution၊ kernel/tool version နဲ့ permission ကို ဖော်ပြထားပါလိမ့်မယ်။ Risk မြင့်တဲ့ Lab ကို disposable VM မှာပဲ လုပ်ပါ။
3. **ခွင့်ပြုချက်ရှိတဲ့ environment ကို သုံးပါ။** ကိုယ်ပိုင် local စက် (သို့) ခွင့်ပြုချက်ရှိတဲ့ non-production environment မှာပဲ စမ်းပါ။ အလုပ်သုံး production server ပေါ်မှာ မစမ်းပါနဲ့။
4. **Command က ဘာလုပ်မလဲ ဖတ်ပါ။** Read-only လို့ ထင်ရတဲ့ command တချို့တောင် process အသစ် စတင်နိုင်ပါတယ်။ File၊ configuration (သို့) persistent data ပြောင်းမပြောင်း နားလည်ပြီးမှ run ပါ။
5. **Cleanup ကို မမေ့ပါနဲ့။** Lab ပြီးရင် ဖော်ပြထားတဲ့ cleanup step တွေကို လိုက်လုပ်ပါ။ ဘာလုပ်နေမှန်း မသိတဲ့ process (သို့) resource ကို ကိုယ့်သဘောနဲ့ မဖျက်ပါနဲ့။

**အထူးသတိပြုရန်:**

- `sudo` နဲ့ အတင်း run မလုပ်ပါနဲ့။ `Operation not permitted` ပေါ်ရင် SELinux ကို disable လုပ်တာ၊ host security setting ကို လျှော့တာမျိုး မလုပ်ပါနဲ့။ Lab ကို ရပ်ပြီး permission၊ kernel support နဲ့ policy ကို စစ်ပါ။
- Rootful Docker daemon ကို ထိန်းချုပ်နိုင်တာ (ဥပမာ Docker socket ကို ချိတ်တာ၊ `docker` group ထဲ ဝင်တာ) က host ပေါ်မှာ root-level privilege ရနိုင်တဲ့ အန္တရာယ်ရှိပါတယ်။ Lab တွေအတွက် အဲဒီလို permission မလိုအပ်ပါဘူး။
- ကိုယ်ပိုင်ခွင့်ပြုချက်မရှိတဲ့ container (သို့) remote runtime ကို မစစ်ဆေးပါနဲ့။

Command ရဲ့ output က kernel version၊ distribution၊ runtime setting၊ namespace configuration နဲ့ `/proc` mount အပေါ် မူတည်ပြီး ကွာနိုင်ပါတယ်။ နမူနာ output နဲ့ ကိုယ့်စက်က output မတူတိုင်း မှားတယ်လို့ မဆိုလိုပါဘူး။ ဘာကြောင့် ကွာသလဲဆိုတာ စဉ်းစားပါ။

## စာအုပ်ထဲက ပုံစံတွေကို ဘယ်လိုဖတ်မလဲ

- **Technical term:** `namespace`၊ `cgroup`၊ system call၊ OCI လို အမည်တွေကို ရှာဖွေရလွယ်အောင် English အတိုင်း ထားပါတယ်။ ပထမဆုံးတွေ့တဲ့နေရာမှာ မြန်မာလို ရှင်းပြထားပါတယ်။ Glossary ကို နောက်မှ ပြင်ဆင်ပါမယ်။
- **Command နဲ့ code:** Terminal command၊ file path နဲ့ code တွေကို code block ထဲမှာ ဖော်ပြထားပါတယ်။ Run မယ့်အခါ Lab ရဲ့ prerequisite နဲ့ safety note ကို အရင်ဖတ်ပါ။
- **Table နဲ့ diagram:** အရာနှစ်ခုကို နှိုင်းယှဉ်တဲ့အခါ၊ component တွေ ဘယ်လိုဆက်နွယ်သလဲ ပြတဲ့အခါ သုံးထားပါတယ်။ Diagram တချို့က သဘောတရားကို ရှင်းပြတဲ့ conceptual diagram ဖြစ်လို့ implementation အားလုံးကို အပြည့်အစုံ မပြနိုင်ပါဘူး။
- **References:** Technical claim တွေကို manual၊ Linux kernel documentation၊ OCI specification (သို့) product documentation နဲ့ ချိတ်ထားပါတယ်။ Version အလိုက် ကွာနိုင်တဲ့ အချက်တွေမှာ version ကိုပါ ကြည့်ပါ။

## စတင်ဖတ်ရန်

[Home](index.md) မှာ Part နဲ့ Chapter တွေ ဘယ်လိုစီထားသလဲ၊ လက်ရှိ ဘယ်အခန်းတွေ ရှိပြီလဲ ကြည့်နိုင်ပါတယ်။ [Preface](preface.md) မှာ စာအုပ်ရဲ့ ရည်ရွယ်ချက်ကို ဖတ်နိုင်ပြီး အဆင်သင့်ဖြစ်ရင် [Chapter 01 — Understanding Containers](part-01-fundamentals/chapter-01-understanding-containers.md) ကနေ စတင်ပါ။

Lab တစ်ခုကို အောင်မြင်စွာ run နိုင်တာနဲ့ container ရဲ့ security အားလုံး မှန်ကန်ကြောင်း သက်သေပြပြီးသား မဟုတ်ပါဘူး။ Lab တစ်ခုချင်းစီက ဘာကို စစ်ဆေးထားသလဲ၊ ဘာကို မစစ်ဆေးထားဘူးလဲဆိုတာကို သီးခြားစဉ်းစားပါ။
