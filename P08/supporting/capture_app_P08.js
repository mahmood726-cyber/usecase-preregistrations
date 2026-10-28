/* P08 v4 full-precision capture; NOT EXECUTED here.
 * Use only in the validated post-release session, after fitting.
 * lnGamma/betaCF/betaInc/tTwoSidedP below are verbatim pinned page text.
 * This helper never fits a model or substitutes R output.
 */
(function () {
  'use strict';
    function lnGamma(x) {
      const cof=[76.18009172947146,-86.50532032941677,24.01409824083091,-1.231739572450155,1.208650973866179e-3,-5.395239384953e-6];
      let y=x, tmp=x+5.5;
      tmp -= (x+0.5)*Math.log(tmp);
      let ser=1.000000000190015;
      for (let j=0;j<6;j++) { y+=1; ser += cof[j]/y; }
      return -tmp + Math.log(2.5066282746310005*ser/x);
    }
    function betaCF(x,a,b) {
      const MAXIT=200, EPS=1e-14, FPMIN=1e-30;
      const qab=a+b, qap=a+1, qam=a-1;
      let c=1, d=1-qab*x/qap;
      if (Math.abs(d)<FPMIN) d=FPMIN;
      d=1/d; let h=d;
      for (let m=1;m<=MAXIT;m++) {
        const m2=2*m;
        let aa=m*(b-m)*x/((qam+m2)*(a+m2));
        d=1+aa*d; if (Math.abs(d)<FPMIN) d=FPMIN;
        c=1+aa/c; if (Math.abs(c)<FPMIN) c=FPMIN;
        d=1/d; h*=d*c;
        aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2));
        d=1+aa*d; if (Math.abs(d)<FPMIN) d=FPMIN;
        c=1+aa/c; if (Math.abs(c)<FPMIN) c=FPMIN;
        d=1/d;
        const del=d*c; h*=del;
        if (Math.abs(del-1)<EPS) break;
      }
      return h;
    }
    function betaInc(a,b,x) {
      if (x<=0) return 0; if (x>=1) return 1;
      const bt = Math.exp(lnGamma(a+b)-lnGamma(a)-lnGamma(b)+a*Math.log(x)+b*Math.log(1-x));
      if (x < (a+1)/(a+b+2)) return bt*betaCF(x,a,b)/a;
      return 1 - bt*betaCF(1-x,b,a)/b;
    }
    function tTwoSidedP(t,df) {
      if (!isFinite(t) || df<=0) return NaN;
      const x = df/(df+t*t);
      return betaInc(df/2, 0.5, x);
    }

  window.P08Capture = Object.freeze({
    primary: function () {
      return window.AlmMetaPlusUI.exportPayload();
    },
    fallback: function () {
      const out = structuredClone(window.__almResults());
      const studies = window._almLastStudies();
      if (out.k !== 10 || studies.length !== 10) throw Error('Expected ten accepted rows');
      const t = out.slope / out.slope_se;
      out.slope_t = t;
      out.slope_p = tTwoSidedP(Math.abs(t), out.hksj_q_df);
      for (const key of ['intercept', 'intercept_se', 'intercept_ci_lb',
                        'intercept_ci_ub', 'slope', 'slope_se', 'slope_ci_lb',
                        'slope_ci_ub', 'tau2_pm', 'hksj_q', 'hksj_q_df',
                        'slope_t', 'slope_p']) {
        if (!Number.isFinite(out[key])) throw Error('Nonfinite browser output: ' + key);
      }
      return {result: out, accepted: structuredClone(studies)};
    }
  });
})();
