# Before You Begin

ဒီစာအုပ်ကို စဖတ်ဖို့ Linux kernel programming ကို ကြိုကျွမ်းကျင်ထားစရာ မလိုပါဘူး။ Terminal မှာ command အနည်းငယ် အသုံးပြုဖူးပြီး file၊ directory နဲ့ process ဆိုတာကို အကြမ်းဖျဉ်း သိထားရင် စလို့ရပါတယ်။ ကျန်တဲ့အကြောင်းအရာတွေကို အခန်းလိုက် ရှင်းပြသွားပါမယ်။

## ၁။ ဘာတွေ ကြိုသိထားရင် ကောင်းမလဲ

အောက်ပါအချက်တွေကို သိထားရင် အခန်းတွေကို လိုက်ဖတ်ရတာ ပိုလွယ်ပါလိမ့်မယ်။ အားလုံးကို အဆင့်မြင့်အထိ သိထားဖို့တော့ မလိုပါဘူး။

- Linux terminal မှာ command ရိုက်ပြီး အခြေခံလုပ်ဆောင်မှုတွေ လုပ်ဖူးခြင်း။
- File နဲ့ directory ဘာကွာသလဲ၊ `/etc/app.conf` လို path တစ်ခုကို ဘယ်လိုဖတ်ရသလဲဆိုတာ သိခြင်း။
- `/etc`၊ `/var` နဲ့ `/proc` လို Linux directory တွေကို အကြမ်းဖျဉ်း သိခြင်း။
- Process တစ်ခု run နေတယ်ဆိုတာနဲ့ PID (Process ID) ရှိတယ်ဆိုတာ နားလည်ခြင်း။
- User၊ group နဲ့ file permission တို့ရဲ့ အခြေခံကို သိခြင်း။
- `cat`၊ `ls`၊ `ps` နဲ့ `uname` လို command တွေကို တစ်ခါတလေ အသုံးပြုဖူးခြင်း။

ဒီအချက်တွေထဲက တချို့ မသိသေးလည်း ပြဿနာမရှိပါဘူး။ အခန်းတစ်ခုထဲမှာ လိုအပ်လာတဲ့အခါ အဓိပ္ပာယ်နဲ့ အသုံးပြုပုံကို ရှင်းပြထားပါမယ်။

## ၂။ Docker ဒါမှမဟုတ် Kubernetes ကြိုသိထားဖို့ လိုသလား

မလိုပါဘူး။ Docker၊ Podman၊ Kubernetes နဲ့ OCI specification တွေကို ကြိုလေ့လာထားစရာ မလိုအောင် အခြေခံကနေ စထားပါတယ်။ Tool တစ်ခုချင်းစီရဲ့ command တွေကို အလွတ်ကျက်ဖို့ထက် အဲဒီ tool တွေအောက်မှာ ဘယ်လို mechanism တွေ အလုပ်လုပ်နေသလဲဆိုတာကို အဓိကထားပါတယ်။ သက်ဆိုင်ရာအခန်းရောက်မှ လိုအပ်တဲ့ tool နဲ့ terminology တွေကို မိတ်ဆက်ပေးပါမယ်။

စာအုပ်ကို ဖတ်ဖို့အတွက် container runtime တစ်ခုကိုလည်း အရင် install လုပ်ထားဖို့ မလိုပါဘူး။ Concept နဲ့ diagram တွေကို ပုံမှန်ဖတ်ရှုနိုင်ပါတယ်။ Lab ကို လက်တွေ့လုပ်ချင်တဲ့အခါမှ သက်ဆိုင်ရာ Lab မှာ ဖော်ပြထားတဲ့ environment နဲ့ tool requirement တွေကို စစ်ပါ။

## ၃။ Lab မလုပ်ခင် အရင်စစ်ပါ

Lab တွေကို စမ်းလုပ်ကြည့်တာက အယူအဆတွေကို ပိုနားလည်စေပါတယ်။ ဒါပေမဲ့ Linux host ပေါ်က command တချို့ဟာ process စတင်တာ၊ file ပြောင်းတာ၊ permission သုံးတာ ဒါမှမဟုတ် system configuration ကို ပြင်တာမျိုး လုပ်နိုင်ပါတယ်။ ဒါကြောင့် command တစ်ခုချင်းစီကို မသိဘဲ ကူးထည့်မလုပ်ပါနဲ့။

Lab တစ်ခုကို မစခင် အောက်ပါအချက်တွေကို အရင်ဖတ်ပါ။

1. **Lab status ကိုကြည့်ပါ။** `Designed, not tested` ဆိုရင် အဲဒီ instruction ကို ဒီစာအုပ်အတွက် သီးခြား environment မှာ run လုပ်ပြီး အတည်မပြုရသေးတာပါ။ စမ်းသပ်ပြီးသားလို့ မယူဆပါနဲ့။
2. **လိုအပ်ချက်ကို စစ်ပါ။** Linux distribution၊ kernel version၊ tool version နဲ့ permission လိုအပ်ချက်တွေကို အဲဒီ Lab ထဲမှာ ဖော်ပြထားပါလိမ့်မယ်။
3. **ကိုယ်ပိုင်ခွင့်ပြုချက်ရှိတဲ့ environment ကို သုံးပါ။** ကိုယ်ပိုင် local စက် ဒါမှမဟုတ် ခွင့်ပြုချက်ရှိတဲ့ non-production environment မှာပဲ စမ်းပါ။ အလုပ်သုံး production server ပေါ်မှာ မစမ်းပါနဲ့။
4. **Command က ဘာလုပ်မလဲ ဖတ်ပါ။** Read-only လို့ ထင်ရတဲ့ command တချို့တောင် process အသစ်စတင်နိုင်ပါတယ်။ File၊ configuration ဒါမှမဟုတ် persistent data ပြောင်းမပြောင်းကို နားလည်ပြီးမှ run ပါ။
5. **Cleanup ကို မမေ့ပါနဲ့။** Lab ပြီးရင် ဖော်ပြထားတဲ့ cleanup step တွေကို လိုက်လုပ်ပါ။ ဘာလုပ်နေမှန်း မသိတဲ့ process ဒါမှမဟုတ် resource ကို ကိုယ့်သဘောနဲ့ မဖျက်ပါနဲ့။

Command ရဲ့ output ဟာ kernel version၊ distribution၊ runtime setting၊ namespace configuration နဲ့ `/proc` mount အပေါ်မူတည်ပြီး ကွာနိုင်ပါတယ်။ နမူနာ output နဲ့ ကိုယ့်စက်က output တူမနေတိုင်း မှားတယ်လို့ မဆိုလိုပါဘူး။ အခန်းထဲမှာ ရှင်းပြထားတဲ့ observation ကို အခြေခံပြီး ဘာကြောင့် ကွာသလဲဆိုတာ စဉ်းစားပါ။

## ၄။ Chapter 01 Lab အတွက် သိထားရန်

Chapter 01 Lab မှာ လက်ရှိ Linux environment ရဲ့ kernel release၊ `/proc` ထဲက PID 1၊ PID namespace နဲ့ cgroup view ကို ကြည့်ပါမယ်။ အဓိက command တွေက `uname`၊ `cat` နဲ့ `readlink` ဖြစ်ပါတယ်။

မိမိပိုင် local rootless Podman container တစ်ခု ရှိပြီး စစ်ဆေးခွင့်ရှိရင် optional အဆင့်အနေနဲ့ `podman exec` ကို သုံးပြီး container အတွင်းက observation ကိုလည်း နှိုင်းယှဉ်နိုင်ပါတယ်။ ဒီ command က container ထဲမှာ process အသစ်တစ်ခု စတင်စေတဲ့အတွက် strictly read-only operation မဟုတ်ပါဘူး။

ဒီ Lab လုပ်တဲ့အခါ—

- Container အသစ် မဖန်တီးပါနဲ့။
- Package အသစ် မတင်ပါနဲ့။
- `sudo` မသုံးပါနဲ့။
- Docker socket permission မပြောင်းပါနဲ့။ `docker` group ထဲလည်း ဝင်ဖို့ မလိုပါဘူး။
- Rootful Docker daemon ကို ချိတ်ပြီး ဒီ Beginner Lab ကို မလုပ်ပါနဲ့။
- ကိုယ်ပိုင်ခွင့်ပြုချက်မရှိတဲ့ container ဒါမှမဟုတ် remote runtime ကို မစစ်ဆေးပါနဲ့။

Rootful Docker daemon ကို ထိန်းချုပ်နိုင်တာဟာ host ပေါ်မှာ root-level privilege ရနိုင်တဲ့ အန္တရာယ်ရှိပါတယ်။ ဒီ Lab အတွက် အဲဒီလို permission မလိုအပ်ပါဘူး။ Optional Podman အဆင့်ကိုလည်း ကိုယ်ပိုင် local rootless container ရှိပြီးသားဖြစ်မှသာ လုပ်ပါ။

**လက်ရှိ Lab status — Designed, not tested.** ဒီ Lab ကို ဒီစာအုပ်အတွက် သီးခြား Linux host ဒါမှမဟုတ် VM မှာ လက်တွေ့ run လုပ်ပြီး ရလဒ်အတည်ပြုထားခြင်း မရှိသေးပါ။ အခန်းထဲမှာ ဖော်ပြထားတဲ့ expected observation တွေဟာ ရလဒ်ကို ဘယ်လိုဖတ်ရမလဲဆိုတာ ရှင်းပြထားတာဖြစ်ပြီး စမ်းသပ်ပြီးသား output မဟုတ်ပါဘူး။

## ၅။ Host နဲ့ Virtual Machine အကြောင်း

ဒီစာအုပ်အတွက် သုံးမယ့် host operating system၊ VM software နဲ့ Fedora guest baseline ကို အခုအချိန်မှာ အတည်မပြုရသေးပါဘူး။ ဒါကြောင့် စာဖတ်သူတိုင်းမှာ တူညီတဲ့ Linux version ဒါမှမဟုတ် VM တစ်ခု ရှိရမယ်လို့ မဆိုလိုပါဘူး။

Lab တစ်ခုချင်းစီမှာ လိုအပ်တဲ့ environment နဲ့ version ကို သီးခြားဖော်ပြပါမယ်။ အဲဒီလိုအပ်ချက်တွေ မပြည့်သေးရင် ကိုယ့်နေ့စဉ်သုံး host ပေါ်မှာ privileged command တွေကို အစားထိုးစမ်းတာမျိုး မလုပ်ပါနဲ့။ Lab ကို မလုပ်နိုင်သေးရင်လည်း အဲဒီအခန်းရဲ့ explanation နဲ့ diagram တွေကို ဆက်ဖတ်နိုင်ပါတယ်။

## ၆။ စာအုပ်ထဲက ပုံစံတွေကို ဘယ်လိုဖတ်မလဲ

စာအုပ်တစ်လျှောက်မှာ ဒီလိုပုံစံတွေကို တွေ့ရပါလိမ့်မယ်။

- **Technical term:** `namespace`၊ `cgroup`၊ system call နဲ့ OCI လို အမည်တွေကို ရှာဖွေရလွယ်အောင် English အတိုင်း ထားပါတယ်။ ပထမဆုံးတွေ့တဲ့နေရာမှာ မြန်မာလို ရှင်းပြထားပါတယ်။
- **Command နဲ့ code:** Terminal command၊ file path နဲ့ code တွေကို code block ထဲမှာ ဖော်ပြထားပါတယ်။ လုပ်ဆောင်မီ Lab ရဲ့ prerequisite နဲ့ safety note ကို အရင်ဖတ်ပါ။
- **Table နဲ့ diagram:** အရာနှစ်ခုကို နှိုင်းယှဉ်တဲ့အခါ၊ component တွေ ဘယ်လိုဆက်နွယ်နေသလဲဆိုတာ ပြတဲ့အခါ သုံးထားပါတယ်။ Diagram တချို့ဟာ အခြေခံသဘောတရားကို ရှင်းပြတဲ့ conceptual diagram ဖြစ်ပြီး implementation အားလုံးကို အပြည့်အစုံ မပြနိုင်ပါဘူး။
- **References:** Technical claim တွေကို သက်ဆိုင်ရာ manual၊ Linux kernel documentation၊ OCI specification ဒါမှမဟုတ် product documentation နဲ့ ချိတ်ထားပါတယ်။ Version အလိုက် ကွာနိုင်တဲ့အချက်တွေမှာ version ကိုပါ ကြည့်ပါ။

## ၇။ ဘယ်အစီအစဉ်နဲ့ ဖတ်သင့်သလဲ

အခုမှ စဖတ်မယ်ဆိုရင် ဒီအစီအစဉ်အတိုင်း သွားလို့ရပါတယ်။

1. [Preface](preface.md) ကိုဖတ်ပြီး စာအုပ်ရဲ့ ရည်ရွယ်ချက်ကို သိအောင်လုပ်ပါ။
2. [Home](index.md) မှာ Part နဲ့ Chapter တွေ ဘယ်လိုစီထားသလဲဆိုတာ ကြည့်ပါ။
3. ဒီစာမျက်နှာက prerequisite နဲ့ Lab safety ကို ဖတ်ပါ။
4. [Chapter 01 — Understanding Containers](part-01-fundamentals/chapter-01-understanding-containers.md) ကနေ စတင်ပါ။
5. မရင်းနှီးတဲ့ term တွေ့ရင် အခန်းထဲက ရှင်းပြချက်နဲ့ references ကို ပြန်ကြည့်ပါ။

Lab တစ်ခုကို အောင်မြင်စွာ run လုပ်နိုင်တာနဲ့ container ရဲ့ security အားလုံး မှန်ကန်ကြောင်း သက်သေပြပြီးသား မဟုတ်ပါဘူး။ Lab တစ်ခုချင်းစီမှာ ဘာကို စစ်ဆေးထားသလဲ၊ ဘာကို မစစ်ဆေးထားဘူးလဲဆိုတာကို သီးခြားစဉ်းစားပါ။
