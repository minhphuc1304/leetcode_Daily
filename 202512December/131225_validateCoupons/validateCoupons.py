class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        Validates and sorts coupons based on business line priority
        
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        # Business line priority mapping
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        valid_coupons = []
        
        # Filter valid coupons
        for i in range(len(code)):
            coupon_code = code[i]
            business = businessLine[i]
            active = isActive[i]
            
            # Validation conditions:
            # 1. Coupon must be active
            # 2. Business line must be recognized
            # 3. Code must be non-empty
            # 4. Code must contain only alphanumeric characters and underscores
            if (active and 
                business in priority and 
                coupon_code and 
                all(char.isalnum() or char == "_" for char in coupon_code)):
                
                valid_coupons.append((priority[business], coupon_code))
        
        # Sort by business line priority
        valid_coupons.sort()
        
        # Extract just the coupon codes
        return [coupon_code for _, coupon_code in valid_coupons]
