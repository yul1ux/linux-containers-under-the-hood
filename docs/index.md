# Linux Containers Under the Hood

Container တစ်ခုကို `docker run` ဒါမှမဟုတ် `podman run` နဲ့ စတင်အသုံးပြုဖူးပါသလား။ Command ရိုက်လိုက်တာနဲ့ application က အလုပ်လုပ်သွားပေမဲ့ နောက်ကွယ်မှာ ဘာတွေဖြစ်နေလဲဆိုတာ စဉ်းစားကြည့်ဖူးပါသလား။ Process တွေကို ဘယ်သူက စီမံပေးနေတာလဲ။ Container တစ်ခုက host ရဲ့ filesystem ကို ဘယ်လိုမြင်သလဲ။ Memory နဲ့ CPU ကို ဘယ်လိုကန့်သတ်ထားသလဲ။ Image နဲ့ runtime က ဘာကွာသလဲ။

ဒီစာအုပ်မှာ အဲဒီမေးခွန်းတွေကို တစ်ခုချင်း လိုက်ဖြေသွားပါမယ်။ Container tool တွေရဲ့ command တွေကိုပဲ လေ့လာမှာ မဟုတ်ဘဲ အောက်ခံ Linux kernel၊ process၊ filesystem၊ networking နဲ့ runtime တွေ ဘယ်လိုအလုပ်လုပ်နေသလဲဆိုတာအထိ ကြည့်သွားမှာပါ။

## ဒီစာအုပ်မှာ ဘာတွေပါသလဲ

စာအုပ်ကို Part ၆ ပိုင်း၊ Chapter ၁၉ ခန်းနဲ့ ဖွဲ့ထားပါတယ်။ အခြေခံအယူအဆကနေ kernel mechanism တွေဆီ၊ အဲဒီကနေ runtime နဲ့ ecosystem ဆီ တစ်ဆင့်ချင်း သွားပါမယ်။

| အပိုင်း | လေ့လာမယ့်အကြောင်းအရာ | Chapter |
|---|---|---:|
| Part I — Container Fundamentals | Container ဆိုတာဘာလဲ၊ VM နဲ့ ဘာကွာလဲ၊ Linux process နဲ့ system call တွေ ဘယ်လိုဆက်စပ်သလဲ | 1–2 |
| Part II — Linux Kernel and Isolation | Namespace၊ cgroup၊ capability နဲ့ filesystem isolation | 3–6 |
| Part III — Filesystem and Networking | OverlayFS၊ image storage နဲ့ container networking | 7–8 |
| Part IV — OCI and Container Runtime Internals | OCI specification၊ `runc`၊ `crun`၊ `containerd` နဲ့ Docker Engine | 9–13 |
| Part V — Security and Operations | Container security၊ rootless container နဲ့ troubleshooting | 14–16 |
| Part VI — Ecosystem and Capstone | Podman၊ Kubernetes runtime architecture နဲ့ ကိုယ်ပိုင် Linux container runtime တည်ဆောက်ခြင်း | 17–19 |

## ဘယ်ကနေ စဖတ်ရမလဲ

ပထမဆုံး [Preface](preface.md) ကို ဖတ်ကြည့်ပါ။ ဒီစာအုပ်ကို ဘာကြောင့်ရေးထားသလဲ၊ ဘယ်သူတွေအတွက် ရည်ရွယ်ထားသလဲဆိုတာ သိရပါလိမ့်မယ်။ ပြီးရင် [Before You Begin](before-you-begin.md) ကို ဖတ်ပါ။ အဲဒီမှာ လိုအပ်တဲ့ Linux အခြေခံ၊ Lab တွေကို ဘယ်လိုဖတ်ပြီး ဘယ်လိုလုံခြုံစွာ လုပ်ဆောင်ရမလဲဆိုတာ ရှင်းပြထားပါတယ်။

ပြီးရင် [Chapter 01 — Understanding Containers](part-01-fundamentals/chapter-01-understanding-containers.md) ကနေ စတင်နိုင်ပါတယ်။ အခန်းတွေကို အစဉ်လိုက် ဖတ်ဖို့ အကြံပြုပါတယ်။ နောက်ပိုင်းမှာ တွေ့လာမယ့် namespace၊ cgroup နဲ့ runtime အကြောင်းတွေဟာ အရင်အခန်းတွေက process နဲ့ kernel အခြေခံတွေပေါ်မှာ တည်ဆောက်ထားလို့ပါ။

## ဒီစာအုပ်ကို ဘယ်လိုရေးထားသလဲ

နည်းပညာအကြောင်းအရာတစ်ခုကို definition နဲ့ပဲ စမရှင်းဘဲ လက်တွေ့မှာ ဘာပြဿနာဖြစ်တတ်သလဲဆိုတာကနေ စတင်ရှင်းပြဖို့ ကြိုးစားထားပါတယ်။ ဥပမာတစ်ခုနဲ့ စိတ်ကူးကြည့်ပြီးမှ အဓိပ္ပာယ်၊ အလုပ်လုပ်ပုံနဲ့ တခြား mechanism တွေနဲ့ ဆက်စပ်ပုံကို ဆက်လေ့လာပါမယ်။

Linux kernel API၊ command၊ file path နဲ့ OCI terminology တွေကို ရှာဖွေရလွယ်အောင် မူရင်း English အတိုင်း ထားပါတယ်။ လိုအပ်တဲ့နေရာမှာတော့ မြန်မာလို အဓိပ္ပာယ်ဖွင့်ပြီး ရှင်းပြထားပါတယ်။ Table နဲ့ diagram တွေကိုလည်း အချက်အလက်များကို နှိုင်းယှဉ်ဖို့၊ component တွေရဲ့ ဆက်နွယ်ပုံကို မြင်သာစေဖို့ အသုံးပြုထားပါတယ်။

တစ်ခု သတိထားရမှာက Linux kernel က သတ်မှတ်ထားတဲ့ behavior နဲ့ Docker၊ Podman လို tool တစ်ခုချင်းစီရဲ့ implementation ဟာ အမြဲတူတာ မဟုတ်ပါဘူး။ အဲဒီနှစ်မျိုးကို ရောမသွားအောင် ခွဲပြီး ရှင်းပြထားပါတယ်။ Version အလိုက် ကွာနိုင်တဲ့အချက်တွေမှာ သက်ဆိုင်ရာ documentation နဲ့ specification ကို ကိုးကားထားပါတယ်။

## လက်ရှိအခြေအနေ

စာအုပ်ကို အခန်းလိုက် ရေးသားနေဆဲဖြစ်ပါတယ်။ လက်ရှိမှာ Chapter 01 ကို manuscript အဖြစ် ထည့်သွင်းထားပြီး Chapters 02–19 ကို ဆက်လက်ရေးသားဖို့ ကျန်နေပါသေးတယ်။ Navigation ထဲမှာ Chapter တစ်ခုရဲ့ ခေါင်းစဉ်ရှိနေတာက အဲဒီအခန်းရဲ့ စာမူအပြည့်အစုံ ပြီးပြီလို့ မဆိုလိုပါဘူး။

Lab တွေကိုလည်း စာရေးပြီးတာနဲ့ စမ်းသပ်ပြီးပြီလို့ မယူဆပါနဲ့။ Chapter 01 Lab ဟာ လက်ရှိမှာ **Designed, not tested** ဖြစ်ပါတယ်။ Lab တစ်ခုချင်းစီရဲ့ အခြေအနေကို အဲဒီအခန်းထဲမှာ သီးခြားဖော်ပြထားပါမယ်။

## စတင်ဖတ်ရှုရန်

- [Preface — စာအုပ်အကြောင်း](preface.md)
- [Before You Begin — မစတင်မီ သိထားရန်](before-you-begin.md)
- [Chapter 01 — Understanding Containers](part-01-fundamentals/chapter-01-understanding-containers.md)
